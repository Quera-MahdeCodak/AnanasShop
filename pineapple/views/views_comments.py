from django.shortcuts import render, redirect, get_object_or_404

from pineapple.models import Comment, Seller
from pineapple.forms import CommentForm

def comment_list_view(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comments_list.html', {'comments': comments})

def seller_comment_list_view(request, certificate_code):
    seller = Seller.objects.get(certificate_code=certificate_code)
    comments = Comment.objects.filter(seller=seller)
    return render(request, 'comments/seller_comment_list.html', {'comments': comments, 'seller': seller})

def comment_create_view(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            selectedSeller=Seller.objects.get(id=form.cleaned_data['seller'])
            obj = Comment.objects.create(seller=selectedSeller,name=form.cleaned_data['name'],text=form.cleaned_data['text'])
            obj.save()
            return redirect('pineapple:comment-list')
    else:
        try:
            form = CommentForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'comments/comment_create.html', {'form': form})
