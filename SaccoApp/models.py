from django.db import models


class Member(models.Model):
member_id = models.CharField(max_length=10)



class Transaction(models.Model): member = models.ForeignKey(Member, on_delete=models.CASCADE)

    transaction_type = models.CharField(max_length=10)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)

latest_transaction = Transaction.objects.latest('id')

if latest_transaction:
    member = latest_transaction.member
    balance = member.balance
else:
    # Handle the case where no transaction was found
    balance = None

def __str__(self):
        return f'{self.transaction_type} - {self.member_id} - {self.amount} - {self.timestamp}'

from rest_framework





#from django.db import models

#class SaccoMember(models.Model):
    #member_id = models.CharField(max_length=20, unique=True)
    #balance = models.DecimalField(max_digits=10, decimal_places=2)

#class SaccoTransaction(models.Model):
  #  member = models.ForeignKey(SaccoMember, on_delete=models.CASCADE)
   # transaction_type = models.CharField(max_length=20)
    #timestamp = models.DateTimeField(auto_now_add=True)