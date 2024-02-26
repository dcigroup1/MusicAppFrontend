from django.views.generic import DetailView
from django.views.generic import TemplateView, ListView, DetailView
import requests
from .utils import get_deezer_album_info


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = 'http://127.0.0.1:7000/api/simple/'
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            formatted_data = [
                {'title': item['title'], 'artist': item['artist'], 'year': item['year']} for item in api_data]

            context['api_data'] = formatted_data

        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context


class BaseRecordView(TemplateView):
    template_name = "records.html"

    def retrieve_album_info(self, deezer_id):
        return get_deezer_album_info(deezer_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = 'http://127.0.0.1:7000/api/all/'
        token = '7beaf66a980341f602e5cdc1d76abbe61aaf0751'

        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            api_data = response.json()

            for item in api_data:
                deezer_id = item['deezer_id']
                deezer_info = self.retrieve_album_info(deezer_id)
                item.update(deezer_info)

            formatted_data = [
                {'title': item['title'], 'artist': item['artist'], 'year': item['year'], 'genre': item['genre'], 'price': item['price'], 'available_units': item['available_units'], 'deezer_id': item['deezer_id']} for item in api_data]

            context['api_data'] = api_data
            context['formatted_data'] = formatted_data

        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context


class DetailRecordView(DetailView):
    template_name = 'record_details.html'
    context_object_name = 'record'
    model = None

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_id = self.kwargs.get('pk')
        url = f'http://127.0.0.1:7000/api/all/{record_id}/'

        token = '7beaf66a980341f602e5cdc1d76abbe61aaf0751'
        headers = {'Authorization': f'Token {token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            record_data = response.json()
            context['record'] = record_data
        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context
