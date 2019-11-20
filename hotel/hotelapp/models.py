from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_fname=models.CharField(max_length=200,help_text="enter the firstname")
    customer_lname=models.CharField(max_length=200,help_text="enter the lname")
    customer_address=models.CharField(max_length=200,help_text="enter the address")
    customer_pno=models.IntegerField(help_text="enter the phone number")

    def __str__(self):
        return str(self.customer_fname)


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100,help_text="enter the name of hotel")
    hotel_city=models.CharField(max_length=200,help_text="enter the city")
    hotel_state=models.CharField(max_length=100)
    hotel_pno=models.IntegerField(help_text="enter the phone number")


    def __str__(self):
        return str(self.hotel_name)

class Rooms(models.Model):
    room_type=models.CharField(max_length=200,help_text="enter the type of room")
    room_rate=models.IntegerField(help_text="enter the room rate")

    def __str__(self):
        return str(self.room_type)

class Reservation(models.Model):
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    room_status=models.CharField(max_length=200,help_text="enter the status")
    noof_guest=models.IntegerField(help_text="enter the no of guests")
    reservation_date=models.DateField(max_length=200)
    customer_fname=models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.checkin_date)

class Billing(models.Model):
    room_chrage=models.IntegerField(help_text="enter the room charge")
    maintaince_charge=models.IntegerField(help_text="enter the maintance charge")
    payment_date=models.DateField(max_length=200)
    customer_fname=models.ForeignKey(Customer,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.room_chrage)



