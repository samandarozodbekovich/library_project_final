from rest_framework.exceptions import ValidationError
from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'subtitle', 'content','author', 'isbn', 'price']
        
    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author',None)
        title = title.replace(" ",'')  
        #check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError({
                'status':False,
                'message':'Kitob sarlafhasi faqat harflardan tashkil topishi lozim!'   
            })
            
        #check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
             raise ValidationError({
                'status':False,
                'message':"Kitob sarlafhasi va Mualifi bir xil bo'lishi lozim"   
            })
             
        return data
    
    def validate_price(self, price):
        if price < 0 or price > 999999999999:
            raise ValidationError({
                'status':False,
                'message':"Kitob narxi xato kiritilgan"   
            })
            
    