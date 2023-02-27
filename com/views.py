
from django.shortcuts import render
from.models import Contact
# Create your views here.
def index (request):
    return render(request,'index.html')

def Gallery (request):
    return render(request,'Leather-Bags-Gallery.html')



def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})

def About (request):
    return render(request,'About.html')

def Product (request):
    return render(request,'Leather-Bag-Manufacturer.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Backpacks (request):
    return render(request,'Leather-backpack.html')

def Sling (request):
    return render(request,'leather-sling-bags-manufacturer.html')

def Totebag (request):
    return render(request,'Leather-tote-bag.html')

def Messangerbag (request):
    return render(request,'leather-messanger-bag.html')


def Laptopbag (request):
    return render(request,'leather-laptop-bags.html')


def Leatherbriefcasebag (request):
    return render(request,'leather-briefcase-bag.html')


def Leatherwashbag (request):
    return render(request,'toiletry-bag.html')



def Leathersaddlebag (request):
    return render(request,'Leather-Saddle-Bags.html')


def Leatherhobobag (request):
    return render(request,'Leather-hobo-bag.html')


def Leatherjournal (request):
    return render(request,'leather-journal-manufacturer.html')



def Leatherdiarymanufacturer (request):
    return render(request,'leather-diary-manufacturer.html')


def Leatherembossed (request):
    return render(request,'Leather-embossed-manufacturer.html')


def Leatherdiary (request):
    return render(request,'Leather-diary.html')



def Jacketsmaen (request):
    return render(request,'Jackets-for-men.html')

def Jacketswomen (request):
    return render(request,'Jackets-for-women.html')

def Leatherwallet (request):
    return render(request,'leather-wallet.html')

def Leatherapron (request):
    return render(request,'leather-apron.html')


def Leatheraccories (request):
    return render(request,'Leather-accories.html')


def Leathercustion (request):
    return render(request,'Leather-Cushion-Cover.html')


def Womenslingbag (request):
    return render(request,'sling-bags-women.html')



def Womenbackpacks (request):
    return render(request,'leather-women-backpacks.html')


def WomenLaptopbag (request):
    return render(request,'women-laptop-bag.html')


def Womenpurses (request):
    return render(request,'leather-women-purses-clutches.html')



def Womentravelbag (request):
    return render(request,'Leather-women-travel-bag')


def Menslingbag (request):
    return render(request,'leather-sling-bag-for-men.html')


def Menbackpack (request):
    return render(request,'leather-men-backpacks.html')



def Menlaptopbags (request):
    return render(request,'men-laptop-bag.html')

def Belts (request):
    return render(request,'leather-belts.html')

def Wallet (request):
    return render(request,'wallet-maker-online.html')

def Mentravelbags (request):
    return render(request,'Leather-men-travel-bag.html')


def Laptopbag (request):
    return render(request,'leather-laptop-bags.html')


def Bikebag (request):
    return render(request,'Bike.html')


def Travelbag (request):
    return render(request,'leather-travel-bags.html')



def Toiletrybag (request):
    return render(request,'toiletry-bag.html')


def Cushion (request):
    return render(request,'cushion.html')


def Camera (request):
    return render(request,'camera-bag.html')



def Leatheraprons (request):
    return render(request,'leather-apron-manufacturer.html')
# seo pages

def Austrilianbag (request):
    return render(request,'australian-leather-bags-manufacturer.html')


def Melbournebag (request):
    return render(request,'bag-manufacturer-melbourne.html')




def Bestleatherindia (request):
    return render(request,'best-leather-bag-manufacturers-in-india.html')

def Bestwalletmanu (request):
    return render(request,'best-wallet-manufacturers-in-india.html')

def Brandedbag (request):
    return render(request,'cheap-branded-bags-in-germany.html')

def Lusa (request):
    return render(request,'cheap-leather-bags-in-usa.html')


def ChaapL (request):
    return render(request,'cheap-leather-bag.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def CLBA (request):
    return render(request,'custom-bag-manufacturers-australia.html')



def CLB (request):
    return render(request,'custom-leather-bag-manufacturers.html')


def CLI (request):
    return render(request,'customized-leather-bags-india.html')


def GLB (request):
    return render(request,'german-leather-bags.html')



def HLB (request):
    return render(request,'handmade-leather-bag-in-usa.html')


def LBM (request):
    return render(request,'handmade-leather-bag-manufacturer.html')


def LBMA (request):
    return render(request,'handmade-leather-bag-manufacturer-australia.html')
def LBF (request):
    return render(request,'handmade-leather-bag-manufacturer-france.html')


def LBC (request):
    return render(request,'handmade-leather-bag-manufacturer-in-canada.html')




def LBCUK (request):
    return render(request,'handmade-leather-bag-manufacturer-uk.html')

def LBCMU (request):
    return render(request,'handmade-leather-bag-manufacturer-usa.html')

def LBAGS (request):
    return render(request,'handmade-leather-bag-manufacturers.html')

def LIND (request):
    return render(request,'handmade-leather-manufacturer-in-india.html')


def LBSY (request):
    return render(request,'handmade-leather-bags-sydney.html')


def INDB (request):
    return render(request,'leather-bags-manufacturers-in-india.html')


def BAGUSA (request):
    return render(request,'leather-bag-manufacturers-usa.html')



def NEAR (request):
    return render(request,'leather-bag-manufacturers-near-me.html')


def UK (request):
    return render(request,'leather-bag-manufacturer-uk.html')


def Italy (request):
    return render(request,'leather-bag-manufacturer-italy.html')



def France (request):
    return render(request,'leather-bag-manufacturer-france.html')


def Canada (request):
    return render(request,'leather-bag-manufacturer-canada.html')


def Austrilia (request):
    return render(request,'leather-bag-manufacturer-australia.html')


def GER (request):
    return render(request,'leather-bag-manuafacurer-germany.html')


def EUR (request):
    return render(request,'leather-goods-manufactuer-europe.html')




def LGM (request):
    return render(request,'leather-goods-manufacturer.html')

def GAUS (request):
    return render(request,'leather-goods-manufacturer-australia.html')

def GGer (request):
    return render(request,'leather-goods-manufacturer-germany.html')

def Dgusa (request):
    return render(request,'leather-goods-manufacturer-in-usa.html')


def Indg (request):
    return render(request,'leather-goods-manufacturer-in-india.html')


def Gc (request):
    return render(request,'leather-goods-manufacturer-in-canada.html')


def LBG (request):
    return render(request,'handmade-leather-bag-manufacturer-germany.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')




def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')




def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')




def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')

def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')



def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')


def Duffle (request):
    return render(request,'leather-duffle-bags.html')