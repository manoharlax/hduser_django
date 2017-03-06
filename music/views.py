from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()
'''
By default the listview returns all the objects within a variable named as object_list
that we use in index.html to access all the objects stored in it...
 If we want to change the name from object_list then we can do this...
'''


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')












# View code using the functions for views
'''
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album,Song

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
	#try:
	#	album = Album.objects.get(pk = album_id)
	#except Album.DoesNotExist:
	#	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk = album_id)
	return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': "You did not select a valid song",
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})
'''