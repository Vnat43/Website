import folium
from streamlit_folium import st_folium
import streamlit as st

st.title("🗺️ Mes Randonnées")

st.markdown("Retrouvez ici la carte de mes randonnées entre les Pyrénées, l'Auvergne et les Alpes.")

@st.cache_resource
def creer_carte():
    m = folium.Map(
        location=[44.8, 3.5], 
        zoom_start=6,
        tiles="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        attr="OpenTopoMap",
    )

    randos = [
        # --- PYRÉNÉES ---
        {"nom": "Pic d'Escurets", "coord": [43.078, -0.489], "type": "sommet"},
        {"nom": "Chapelle de la Madeleine", "coord": [43.109, -0.865], "type": "sommet"},
        {"nom": "Trône du Roi", "coord": [43.088, -0.630], "type": "sommet"},
        {"nom": "Pic d'Anie", "coord": [42.945, -0.720], "type": "sommet"},
        {"nom": "Pic d'Othy (Orhy)", "coord": [42.988, -1.004], "type": "sommet"},
        {"nom": "Pic de Ger", "coord": [42.942, -0.340], "type": "sommet"},
        {"nom": "Pic de Sesques", "coord": [42.915, -0.495], "type": "sommet"},
        {"nom": "Mailh Massibé", "coord": [43.056, -0.490], "type": "sommet"},
        {"nom": "Pambassibé", "coord": [43.051, -0.492], "type": "sommet"},
        {"nom": "Pic du Montagnon de Bielle", "coord": [43.045, -0.435], "type": "sommet"},
        {"nom": "Pic de la Sagette", "coord": [42.880, -0.395], "type": "sommet"},
        {"nom": "Pic du Montagnon d'Iseye", "coord": [42.966, -0.528], "type": "sommet"},
        {"nom": "Lac d'Ansabère", "coord": [42.885, -0.710], "type": "eau"},
        {"nom": "Lac de Acherito", "coord": [42.879, -0.709], "type": "eau"},
        {"nom": "Lacs d'Ayous", "coord": [42.845, -0.485], "type": "eau"},
        {"nom": "Lac d'Estaens", "coord": [42.798, -0.550], "type": "eau"},
        {"nom": "Lacs du Montagnon", "coord": [42.965, -0.525], "type": "eau"},
        {"nom": "Lac de Gaube", "coord": [42.825, -0.140], "type": "eau"},
        {"nom": "Lac des Gloriettes", "coord": [42.775, 0.035], "type": "eau"},
        {"nom": "Lac de Bious-Artigues", "coord": [42.873, -0.447], "type": "eau"},
        {"nom": "Lac de Fabrèges", "coord": [42.845, -0.383], "type": "eau"},
        {"nom": "Cascade d'Isabe", "coord": [42.955, -0.465], "type": "eau"},
        {"nom": "Cascades du Pont d'Espagne", "coord": [42.850, -0.138], "type": "eau"},
        {"nom": "Cascade de Sanchèse", "coord": [42.915, -0.691], "type": "eau"},
        {"nom": "Aguas Tuertas", "coord": [42.836, -0.612], "type": "eau"},
        {"nom": "Passerelle d'Holzarte", "coord": [43.004, -0.923], "type": "point_vue"},
        {"nom": "Chemin de la Mâture", "coord": [42.888, -0.560], "type": "point_vue"},
        {"nom": "Cirque de Gavarnie", "coord": [42.735, -0.011], "type": "point_vue"},
        {"nom": "Col de Pau", "coord": [42.893, -0.669], "type": "col"},
        {"nom": "Col du Somport", "coord": [42.795, -0.525], "type": "col"},
        {"nom": "Cabane du Boué", "coord": [42.909, -0.633], "type": "patrimoine"},
        {"nom": "Cabane d'Ichéus", "coord": [42.978, -0.691], "type": "patrimoine"},

        # --- AUVERGNE ---
        {"nom": "Puy de Sancy", "coord": [45.528, 2.813], "type": "sommet"},
        {"nom": "Puy Mary", "coord": [45.108, 2.676], "type": "sommet"},
        {"nom": "Mont Mézenc", "coord": [44.912, 4.188], "type": "sommet"},
        {"nom": "Truc de la Garde", "coord": [44.838, 3.342], "type": "sommet"},
        {"nom": "Lac d'Aydat", "coord": [45.666, 2.983], "type": "eau"},
        {"nom": "Lac de Guéry", "coord": [45.626, 2.818], "type": "eau"},
        {"nom": "Cascade du Lac de Guéry", "coord": [45.632, 2.822], "type": "eau"},
        {"nom": "Plateau de Gergovie", "coord": [45.713, 3.123], "type": "point_vue"},

        # --- ALPES : BELLEDONNE / OISANS / MATHEYSINE ---
        {"nom": "Croix de Belledonne", "coord": [45.168, 5.988], "type": "sommet"},
        {"nom": "Croix de Chamrousse", "coord": [45.133, 5.892], "type": "sommet"},
        {"nom": "Grand Colon", "coord": [45.183, 5.913], "type": "sommet"},
        {"nom": "La Peyrouse (Laffrey)", "coord": [45.031, 5.772], "type": "sommet"},
        {"nom": "Lacs Robert", "coord": [45.133, 5.918], "type": "eau"},
        {"nom": "Lac Achard", "coord": [45.116, 5.898], "type": "eau"},
        {"nom": "Lac de Laffrey", "coord": [45.019, 5.777], "type": "eau"},
        {"nom": "Lac du Crozet", "coord": [45.195, 5.922], "type": "eau"},
        {"nom": "Lac du Lauvitel", "coord": [44.966, 6.066], "type": "eau"},
        {"nom": "Lac de Fond de France", "coord": [45.250, 6.100], "type": "eau"},
        {"nom": "Lacs du Doménon", "coord": [45.176, 5.962], "type": "eau"},
        {"nom": "Vertige des Cimes", "coord": [45.133, 5.895], "type": "point_vue"},
        {"nom": "Notre Dame de la Salette", "coord": [44.858, 5.978], "type": "patrimoine"},
        {"nom": "Chêne de Venon", "coord": [45.174, 5.801], "type": "patrimoine"},

        # --- ALPES : CHARTREUSE / VERCORS / SAVOIE ---
        {"nom": "Chamechaude", "coord": [45.286, 5.787], "type": "sommet"},
        {"nom": "Dent de Crolles", "coord": [45.306, 5.864], "type": "sommet"},
        {"nom": "Mont Rachais", "coord": [45.228, 5.748], "type": "sommet"},
        {"nom": "Mont St Eynard", "coord": [45.234, 5.764], "type": "sommet"},
        {"nom": "Charmant Som", "coord": [45.328, 5.766], "type": "sommet"},
        {"nom": "La Pinéa", "coord": [45.292, 5.753], "type": "sommet"},
        {"nom": "Roc Cornafion", "coord": [45.060, 5.586], "type": "sommet"},
        {"nom": "Dent du Loup", "coord": [45.220, 5.625], "type": "sommet"},
        {"nom": "Mont Veyrier", "coord": [45.895, 6.185], "type": "sommet"},
        {"nom": "Dent du Chat", "coord": [45.656, 5.811], "type": "sommet"},
        {"nom": "Le Moucherotte", "coord": [45.147, 5.639], "type": "sommet"},
        {"nom": "Lac d'Annecy", "coord": [45.866, 6.166], "type": "eau"},
        {"nom": "Lac du Bourget", "coord": [45.733, 5.866], "type": "eau"},
        {"nom": "Lac de Monteynard", "coord": [44.908, 5.688], "type": "eau"},
        {"nom": "Cirque de Saint Même", "coord": [45.398, 5.889], "type": "eau"},
        {"nom": "Col Vert", "coord": [45.048, 5.592], "type": "col"},
        {"nom": "Col de l'Arzelier", "coord": [44.961, 5.592], "type": "col"},
        {"nom": "Pas de l'Aiguille", "coord": [44.808, 5.518], "type": "col"},
        {"nom": "Combe Laval", "coord": [45.016, 5.333], "type": "point_vue"},
        {"nom": "Monastère de la Grande Chartreuse", "coord": [45.342, 5.795], "type": "patrimoine"},
    ]

    icones_config = {
        "sommet": {"color": "darkred", "icon": "mountain"},
        "eau": {"color": "blue", "icon": "tint"},
        "col": {"color": "orange", "icon": "arrows-v"},
        "point_vue": {"color": "purple", "icon": "camera"},
        "patrimoine": {"color": "green", "icon": "leaf"}
    }

    for rando in randos:
        config = icones_config.get(rando["type"], icones_config["sommet"])
        icone = folium.Icon(color=config["color"], icon=config["icon"], prefix="fa")
        denivele_text = f"<br><i>{rando['denivele']}</i>" if "denivele" in rando else ""
        
        folium.Marker(
            location=rando["coord"],
            popup=f"<b>{rando['nom']}</b>{denivele_text}",
            tooltip=rando["nom"],
            icon=icone,
        ).add_to(m)
        
    return m

carte_finale = creer_carte()

st_folium(carte_finale, width=1200, height=700, returned_objects=[])

st.divider()

st.subheader("Mes carnets de route")
st.info("Ici viendront bientôt s'ajouter les fiches détaillées et les photos pour chaque randonnée !")