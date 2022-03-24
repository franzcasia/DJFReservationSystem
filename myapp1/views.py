from django.shortcuts import render
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
from myapp1 import views
from django.shortcuts import redirect

# Create your views here.

class MyIndexView(View):
    def get(self,request):
        return render(request, 'index.html')

class MyResView(View):
    def get(self,request):
        return render(request, 'res.html' )

class MyMornView(View):
    def get(self,request):
        return render(request, 'morning.html')
    def post(self, request):        
        form = BookForm(request.POST)  

        if form.is_valid():
            # try:
            res_number = request.POST.get("res_number")
            Name = request.POST.get("Name")
            Address = request.POST.get("Address")
            tel_Number = request.POST.get("tel_Number")
            room_number = request.POST.get("room_number")
            date = request.POST.get("date")
            time = request.POST.get("time")

            form = ResBook(res_number = res_number, Name = Name, Address = Address, tel_Number = tel_Number, room_number = room_number, date = date, time= time)
            form.save()

                 
            return redirect('/res')
          
        else:
            print(form.errors)
            return HttpResponse('not valid')


class CreateRoomView(View):
    def get(self,request):
        return render(request, 'createRoom.html')
    
    def post(self,request):
        form = RoomForm(request.POST)

        if form.is_valid():
            room_number = request.POST.get("room_number")
            room_type = request.POST.get("room_type")
            no_guest = request.POST.get("no_guest")
            form = Room(room_number = room_number,room_type = room_type, no_guest = no_guest)
            form.save()
            return redirect('/Rooms')
        else:
            print(form.errors)    
            return HttpResponse('Please Fill Out All The Information') 

class RoomView(View):
    def get(self, request):
        room = Room.objects.all()
        context = {
            'roomRow' : room
        }
        return render(request, 'Rooms.html', context)

    def post(self, request):
        if(request.method) == 'POST':
            if 'btnUpdate' in request.POST:
                print('update profile')
                room_number = request.POST.get("room_number")
                room_type = request.POST.get("room_type")
                no_guest = request.POST.get("no_guest")
                update = Room.objects.filter(room_number = room_number).update(room_type = room_type, no_guest = no_guest)
                print(update)
                print('Room updated')
                return redirect('/Rooms')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                iddn = request.POST.get("room_number")
                iddn = Room.objects.filter(room_number = iddn).delete()
                print('record deleted')
                return redirect('/Rooms')

class RoomDisplayView(View):
    def get(self, request):
        room = Room.objects.all()
        context = {
            'roomRow' : room
        }
        return render(request, 'RoomsDisplay.html', context)






        
            
         
 
        
    
   


            
        


