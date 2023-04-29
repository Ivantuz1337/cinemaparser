from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import httpx


def reservation(request):
    return render(request, 'reservation.html')

    # return render(request, 'reservation.html', context={'name':'123'})

async def startpage(request):
    url = "https://www.apollokino.ee/schedule"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        html = response.content
    
    soup = BeautifulSoup(html, "html.parser")
    schedule_card_inners = soup.find_all('div', class_='schedule-card__inner')
    films = [[
        i.find(class_='schedule-card__title bold').text.strip(),
        i.find(class_='schedule-card__secondary-title bold text-small').text.strip(),
        i.find(class_='schedule-card__time bold').text.strip(),
        'https://' + str(i.find('img', class_='image__img lazyload').get("data-srcset").split(",", 1)[0].replace(" 350w", ""))
    ] for i in schedule_card_inners]

    return render(request, 'startpage.html', context={'films': films})











































# def parse():
#     url = "https://www.apollokino.ee/schedule"

#     response = requests.get(url)
#     html = response.content

#     soup = BeautifulSoup(html, "html.parser")

#     film_names = [p.text for p in soup.find_all("p", {"class": "schedule-card__title bold"})]

#     return film_names









# def reservation1(request):
#     url = "https://www.apollokino.ee/schedule"
#     response = requests.get(url)
#     html = response.text

#     soup = BeautifulSoup(html, "html.parser")
#     schedule_card_inners = soup.find_all('div', class_='schedule-card__inner')
#     films = [[
#         i.find(class_='schedule-card__title bold').text.strip(),
#         i.find(class_='schedule-card__secondary-title bold text-small').text.strip(),
#         i.find(class_='schedule-card__time bold').text.strip(),
#         i.find('img', class_='image__img lazyload').get("data-srcset").split(",", 1)[0].replace(" 350w", "")
#     ] for i in schedule_card_inners]
# reservation1(1)