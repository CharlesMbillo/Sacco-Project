from django.shortcuts import render

from .models import Member, Transaction
from .serializers import MemberSerializer, TransactionSerializer

from django.shortcuts import render
from django.http import JsonResponse
from .models import Member, Transaction

def sacco_transaction_view(request):
    if request.method == 'POST':
        member_id = request.POST.get('member-id')
        transaction_type = request.POST.get('transaction-type')
        face_amount = request.POST.get('face-amount')
        
        # Process the transaction and update the balance
        transaction = Transaction(
member_id=member_id, transaction_type=transaction_type,                          
            face_amount=face_amount
        )
        transaction.save()

        # Ensure transaction is defined before accessing its member attribute
transaction = Transaction.objects.latest('id')

# Assuming you want to retrieve the last transaction record

if transaction:
    member = transaction.member
    balance = member.balance
else:
    # Handle the case where no transaction was found
    balance = None
    
# Retrieve the related Member instance for the transaction
member = transaction.member

# Now access the balance of the member
balance = member.balance 
balance = transaction.member.balance  

# assume this is the updated balance

# Return the updated balance as a JSON response
return JsonResponse({
    'balance': balance, 
    'transaction': {
        'timestamp': transaction.timestamp
    }
})

    return render(request, 'sacco.html')


def index(request):

    if request.method == 'POST':

        member_id = request.POST.get('member-id')

        transaction_type = request.POST.get('transaction-type')
face_amount = request.POST.get('face-amount')

        

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


from django.utils import timezone


def index(request):

    if request.method == 'POST':

        # ...

        

        # Create a new transaction record with the current date and time

        transaction = Transaction(member=member, transaction_type=transaction_type, face_amount=0, timestamp=timezone.now())  # Set the amount as needed

        transaction.save()

        

        # ...

