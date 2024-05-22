from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "transaction_room"
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        transaction_type = text_data_json['transaction_type']
        member_id = text_data_json['member_id']
        amount = text_data_json['amount']

        member = Member.objects.get(member_id=member_id)

        if transaction_type == "deposit":
            Transaction.objects.create(member=member, transaction_type=transaction_type, amount=amount)
            balance = member.transaction_set.aggregate(balance=models.Sum('amount'))['balance'] or 0
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'send_balance',
                    'balance': balance
                }
            )
        elif transaction_type == "withdrawal":
            Transaction.objects.create(member=member, transaction_type=transaction_type, amount=amount)
            balance = member.transaction_set.aggregate(balance=models.Sum('amount'))['balance'] or 0
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'send_balance',
                    'balance': balance
                }
            )

    async def send_balance(self, event):
        balance = event['balance']
        await self.send(text_data=json.dumps({
            'balance': balance
        }))