import dataclasses
from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass

# Create your views here.

@dataclass
class Pirate:
    name: str
    members: list

@dataclass
class group:
    name: str
    pic: str



context = {
    'groups' : {
        'pirate_groups' : {
            'Shanks' : group("Red Hair Pirates", "static/images/Shanks_logo.png"),
            'Kaido' : group(" The Beast Pirates", "static/images/Kaido_logo.png"),
            'Big Mom' : group("Big Mom Pirates", "static/images/big_mom_logo.webp"),
            'Doflamingo' : group("Doflamingo Pirates", "static/images/Doflamingo_logo.webp"),
            'Luffy' : group("Straw Hat Pirates", "static/images/straw_hat_logo.webp"),
            'Law' : group("The Heart Pirates", "static/images/law_logo.png")
        },
        'Luffy' : {'pirate':Pirate("Luffy's Crew", ['Luffy: 1.5 Billion Berry Bounty (Captain)', 'Jimbei: 438 Million Berry Bounty (Helmsman)', 'Zoro: 320 Million Berry Bounty (First Mate)', 'Sanji: 330 Million Berry Bounty(Cook)', '“God” Usopp: 200 Million Berry Bounty(Sniper)', 'Robin: 130 Million Berry Bounty (Devil Fruit User)', 'Franky: 94 Million Berry Bounty (Shipwright)', 'Brook: 83 Million Berry Bounty (Musician)', 'Nami: 66 Million Berry Bounty (Navigator)', 'Chopper: 100 Berry Bounty (Doctor)'])},
        'Shanks' : {'pirate' : Pirate("Shank's Crew", ['Shanks: 4.048 Billion Berry Bounty (Captain)','Rockstar: 94 million Berry Bounty (Newest Elite Member)','Ben Beckman: N/A (First Mate)','Lucky Roux: N/A (Elite Crew Member)','Yassop: N/A (Sniper)'])},
        'Big Mom' : {'pirate' : Pirate("Big Mom's Crew", ['Linlin “Big Mom”: 4.3 Billion Berry Bounty (Captain)','Katakuri: 1 Billion Berry Bounty (Devil Fruit User)','Smoothie: 932 Million Berry Bounty (Devil Fruit User)','“Thousand Arms”: 860 Million Berry Bounty (Devil Fruit User)','Perespero: 700 Million Berry Bounty'])},
        'Kaido' : {'pirate' : Pirate("Kaido's Crew", ["Kaido: 4.611 Billion Berry Bounty (Captain)", "Queen: 1.3 Billion Berry Bounty (Devil Fruit User)", "King: 1 Billion Berry Bounty (Devil Fruit User)", "Jack: 1 Billion Berry Bounty (Devil Fruit User)"])},
        'Doflamingo' : {'pirate' : Pirate("Doflamingo's Crew", ["Doflamingo: 340 Million Berry Bounty (Captain)", "Bellamy: 195 Million Berry Bounty (Devil Fruit User)", "Trebol: 99 Million Berry Bounty (Devil Fruit User)", "Diamante: 99 Million Berry Bounty (Devil Fruit User)", "Pica: 99 Million Berry Bounty (Devil Fruit User)"])},
        "Law" : {'pirate' : Pirate("Law's Crew", ["Trafalgar D. Water Law: 3 Billion Berry Bounty (Captain)", "Bepo: 500 Berry Bounty (Navigator)", "Penguin: N/A (Member)", "Shachi: N/A (Member)", "Jean Bart: N/A (Member)"])}

    }
}


def base_view(request):
    return render(request, 'home.html', context['groups'])

def pirate_view(request, name):
    return render(request, 'pirates.html', context['groups'][name])