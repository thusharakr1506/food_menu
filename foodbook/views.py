from django.shortcuts import render,redirect

from django.views.generic import View

from foodbook.models import Food

from django import forms

class FoodForm(forms.Form):
    name=forms.CharField()
    category=forms.CharField()
    cuisine=forms.CharField()
    price=forms.IntegerField()

class FoodListView(View):
    def get(self,request,*args,**kwargs):
        qs=Food.objects.all()
        return render(request,"food_list.html",{"data":qs})
    
class FoodDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Food.objects.get(id=id)
        return render(request,"food_detail.html",{"data":qs})
    
class FoodDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Food.objects.get(id=id).delete()
        return redirect("food-list")
    
class FoodCreateView(View):
    def get(self,request,*args,**kwargs):
        form=FoodForm()
        return render(request,"food_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=FoodForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            Food.objects.create(**data)
            return redirect("food-list")
        else:
            return render(request,"food_add.html",{"form":form})

        # data={k:v for k,v in request.POST.items()}

        # data.pop("csrfmiddlewaretoken")

        # Food.objects.create(**data)

        # return redirect("food-list")


class FoodUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        food_object=Food.objects.get(id=id)
        data={
            "name":food_object.name,
            "category":food_object.category,
            "cuisine":food_object.cuisine,
            "price":food_object.price
        }
        form=FoodForm(initial=data)
        return render(request,"food_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=FoodForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Food.objects.filter(id=id).update(**data)
            return redirect("food-list")
        else:
            return render(request,"food_edit.html",{"form":form})
