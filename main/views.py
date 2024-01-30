from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

from main.forms import ProductForm, VersionForm, VersionFormSet
from main.models import Product, Contact, BlogPost, Version

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['object_list']:
            product.active_version = product.versions.filter(is_current=True).first()
        return context


def contacts(request):
    contacts_list = Contact.objects.first()
    context = {
        'object_list': contacts_list,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"{name}({email}):{message}")

    return render(request, 'main/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['version_formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context['version_formset'] = VersionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        version_formset = context['version_formset']
        if version_formset.is_valid():
            version_formset.save()
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:product_detail', kwargs={'pk': self.kwargs['pk']})


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('main:blogpost-list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1

        if self.object.views_count == 100:
            self.send_mail()

        self.object.save()

        return self.object

    def send_mail(self):
        subject = f'{self.object.title} просмотрен {self.object.views_count} раз'
        message = 'Поздравляем!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['bishop81285@gmail.com']

        send_mail(subject, message, from_email, recipient_list)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published', 'views_count',)

    def get_success_url(self):
        return reverse('main:blogpost-detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('main:blogpost-list')
