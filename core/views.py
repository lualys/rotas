from django.shortcuts import render
import folium

def mapa_rota(request):
   
    mapa = folium.Map(location=[-10.441916, -45.176382], zoom_start=14)

    rota_saida = 'geojson/retorno.geojson'
    rota_volta = 'geojson/saida.geojson'
    ponto_1 = 'geojson/paradas-retorno.geojson'
    ponto_2 = 'geojson/paradas-saida.geojson'

    folium.GeoJson(
        rota_saida, name='saida', style_function=lambda x: {"color": "red"}
    ).add_to(mapa)
    folium.GeoJson(rota_volta, name='saida').add_to(mapa)

    folium.GeoJson(ponto_1, name='ponto 1', marker=folium.Marker(
        icon=folium.DivIcon(
            icon_size=(150, 36),
            html='<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAABe0lEQVR4nO2Xz0rDQBCH92l8hsQnyPoHLz36BgWPpngXPNncjWch8Rm0l/GgJ9GmKgiiBxsPVWrpdSS1ewvdTbq72cD8YC5JmPm+ZBIIYxQKhUIxlc2tdM/n6cDn6cznKVqumc+Tay+43K0F7/HkpAFoLK0gOa5z59Gx2lEWWK4NulRekFxVWJ/010GBqbLAfneALhYjgW5LnoBI5+AIi2INpbPu/NYL9KIYi4LbfGXdDyf4mc9x/DXH7OVncezmLsfXt+niWFk9jCbSvmK+UQFT8GBDoA78oyI8mBYwDQ8mBUyuDZgWsAUPJgRswoNuARs7D6YEasE/rQcPOgWagAedAgXU8PlbCV5c55RApnjndcKD7pdYBp9phgedAk3Ag06B1fD/6+W0wNjSzoMNAbzYMFpAApInMFp+UlX/1lTXBGyskIBvnQCreM6ZGb02C4Sn8bZocNg/51qbK/QJJfPljfvxh2gQRmfvqoMrz4nK+8jmUygUCoXpyB/9jx6bE14y5AAAAABJRU5ErkJggg==">'
        )
    )
    ).add_to(mapa)

    folium.GeoJson(ponto_2, name='ponto 1', marker=folium.Marker(
        icon=folium.DivIcon(
            icon_size=(150, 36),
            html='<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAABe0lEQVR4nO2Xz0rDQBCH92l8hsQnyPoHLz36BgWPpngXPNncjWch8Rm0l/GgJ9GmKgiiBxsPVWrpdSS1ewvdTbq72cD8YC5JmPm+ZBIIYxQKhUIxlc2tdM/n6cDn6cznKVqumc+Tay+43K0F7/HkpAFoLK0gOa5z59Gx2lEWWK4NulRekFxVWJ/010GBqbLAfneALhYjgW5LnoBI5+AIi2INpbPu/NYL9KIYi4LbfGXdDyf4mc9x/DXH7OVncezmLsfXt+niWFk9jCbSvmK+UQFT8GBDoA78oyI8mBYwDQ8mBUyuDZgWsAUPJgRswoNuARs7D6YEasE/rQcPOgWagAedAgXU8PlbCV5c55RApnjndcKD7pdYBp9phgedAk3Ag06B1fD/6+W0wNjSzoMNAbzYMFpAApInMFp+UlX/1lTXBGyskIBvnQCreM6ZGb02C4Sn8bZocNg/51qbK/QJJfPljfvxh2gQRmfvqoMrz4nK+8jmUygUCoXpyB/9jx6bE14y5AAAAABJRU5ErkJggg==">'
        )
    )
    ).add_to(mapa)
    

    mapa_renderizado = mapa._repr_html_()

    return render(request, 'index.html', {'mapa': mapa_renderizado})
