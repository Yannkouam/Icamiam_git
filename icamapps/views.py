from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Product, Event, MenuItem, Contact, Panier, Confirmation, Order
from .forms import PanierForm  # Assurez-vous que ce formulaire existe et est correctement défini

# Créez une instance du modèle utilisateur
User = get_user_model()

def home(request):
    events = Event.objects.all()
    menu_items = MenuItem.objects.all()
    contact_info = Contact.objects.first()  # Supposons qu'il n'y a qu'une seule entrée de contact
    return render(request, 'icamapps/home.html', context={
        'events': events,
        'menu_items': menu_items,
        'contact_info': contact_info,
    })

def menu(request):
    # Récupérer tous les produits depuis la base de données
    products = Product.objects.all()
    # Passer les produits au modèle de page HTML
    return render(request, 'icamapps/menu.html', context={"products": products})

def event(request):
    # Récupérer tous les événements depuis la base de données
    events = Event.objects.all()
    # Passer les événements au modèle de page HTML
    return render(request, 'icamapps/event.html', context={"events": events})

@login_required
def panier(request):
    # Récupérer ou créer l'objet Panier de l'utilisateur actuel
    panier, created = Panier.objects.get_or_create(user=request.user)
    form = PanierForm()  # Assurez-vous que ce formulaire existe dans forms.py et est bien importé

    if request.method == 'POST':
        form = PanierForm(request.POST)
        if form.is_valid():
            # Traitez le formulaire si nécessaire
            pass
    
    return render(request, 'icamapps/panier.html', {'panier': panier, 'form': form})

def index(request):
    return render(request, 'icamapps/index.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    panier, _ = Panier.objects.get_or_create(user=request.user)
    
    # Chercher une commande existante pour cet utilisateur et ce produit
    order = Order.objects.filter(user=request.user, product=product).first()

    if order:
        # Si une commande existe, incrémenter la quantité
        order.quantity += 1
        order.save()
    else:
        # Sinon, créer une nouvelle commande et l'ajouter au panier
        order = Order.objects.create(user=request.user, product=product, quantity=1)
        panier.orders.add(order)
        panier.save()
    
    return redirect(reverse("menu"))

@login_required
def remove_from_cart(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)  # Assurez-vous que l'ordre appartient à l'utilisateur
    order.delete()

    # Vérifiez si le nombre d'articles dans le panier est égal à zéro
    if not Order.objects.filter(user=request.user).exists():
        # Si le panier est vide, vous pouvez aussi supprimer l'objet Panier
        panier = Panier.objects.filter(user=request.user).first()
        if panier:
            panier.delete()

    return redirect('panier')

@login_required
def confirmation(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.create(user=request.user, product=product)
    context = {'order_number': order.order_number}
    return render(request, 'icamapps/confirmation.html', context)
