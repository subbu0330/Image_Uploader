from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import ImageForm
from .models import Image


def image_upload_view(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            file = request.FILES.get('image')
            if file:
                instance = Image(image=file)
                instance.save()
                return JsonResponse({'success': True})
            print("SUBBBBBBBBBBBBBBBBBB")
            return JsonResponse({'success': False})
        else:
            form = ImageForm(request.POST, request.FILES)
            files = request.FILES.getlist('image')
            if form.is_valid():
                for f in files:
                    instance = Image(image=f)
                    instance.save()
                return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})




def image_list_view(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def delete_image_view(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'delete_image.html', {'image': image})