from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):

    template_name='products/list.html'
    def get_context_data(self,*args,**kwargs):
        print('inside')
        context=super(SearchProductView,self).get_context_data(*args,**kwargs)
        print(context)
        context['query']=self.request.GET.get('q',None)
        
        return context

    def get_queryset(self,*args,**kwargs):
        request=self.request
        query=request.GET.get('q',None)
        print(query)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.all()