from django.shortcuts import render

from .models import Member, Transaction

from .serializers import MemberSerializer, TransactionSerializer



def index(request):

    if request.method == 'POST':

        member_id = request.POST.get('member-id')

        transaction_type = request.POST.get('transaction-type')

        

        # Perform validation on member_id and transaction_type

        

        # Calculate balance based on deposit, savings, and withdrawal transactions

        deposits = Transaction.objects.filter(member__member_id=member_id, transaction_type='Deposit').aggregate(total=models.Sum('amount'))

        savings = Transaction.objects.filter(member__member_id=member_id, transaction_type='Saving').aggregate(total=models.Sum('amount'))

        withdrawals = Transaction.objects.filter(member__member_id=member_id, transaction_type='Withdrawal').aggregate(total=models.Sum('amount'))

        balance = (deposits['total'] or 0) + (savings['total'] or 0) - (withdrawals['total'] or 0)

        

        # Create a new transaction record

        member = Member.objects.get(member_id=member_id)

        transaction = Transaction(member=member, transaction_type=transaction_type, amount=0)  # Set the amount as needed

        transaction.save()

        

        # Serialize the member and transaction data

        member_serializer = MemberSerializer(member)

        transaction_serializer = TransactionSerializer(transaction)

        

        return render(request, 'index.html', {

            'members': [member_serializer.data],

            'transactions': [transaction_serializer.data],

            'balance': balance

        })

    else:

        members = Member.objects.all()

        transactions = Transaction.objects.all()

        member_serializer = MemberSerializer(members, many=True)

        transaction_serializer = TransactionSerializer(transactions, many=True)

        return render(request, 'index.html', {

            'members': member_serializer.data,

            'transactions': transaction_serializer.data

        })

from django.shortcuts import render

from django.utils import timezone

from .models import Member, Transaction

from .serializers import MemberSerializer, TransactionSerializer



def index(request):

    if request.method == 'POST':

        # ...

        

        # Create a new transaction record with the current date and time

        transaction = Transaction(member=member, transaction_type=transaction_type, amount=0, timestamp=timezone.now())  # Set the amount as needed

        transaction.save()

        

        # ...

