import ezdxf
import shapely
from shapely.geometry import LineString, Point, MultiLineString, Polygon, MultiPolygon


def oku(a1,a2,a3,a4,a5,s,a7,ht,h1,h2,h3,h4,hs,kot):

    #Savak Boyu
    Ls = 12

    # DXF ten Arazi değerleri okunması
    doc = ezdxf.readfile('lwpolyline.dxf')
    msp = doc.modelspace()
    # Yapı Çizimi dosyası oluşturulması
    doc1 = ezdxf.new('R2007',setup=True)
    msp1 = doc1.modelspace()
    # Gerekli Layerların Oluşturulması

    doc1.layers.new(name='Tersip Bendi', dxfattribs={'linetype': 'CONTINUOUS','lineweight':53 ,'color': 1})
    doc1.layers.new(name='Hatch', dxfattribs={'linetype': 'CONTINUOUS', 'color': 8})
    doc1.layers.new(name='Kot', dxfattribs={'linetype': 'CONTINUOUS', 'color': 6})
    doc1.layers.new(name='Yazı', dxfattribs={'linetype': 'CONTINUOUS', 'color': 2})
    doc1.layers.new(name='Arazi', dxfattribs={'linetype': 'DASHED', 'color': 6})
    doc1.layers.new(name='Savak', dxfattribs={'linetype': 'CONTINUOUS', 'lineweight':40 , 'color': 3})
    doc1.layers.new(name='Boru', dxfattribs={'linetype': 'CONTINUOUS' , 'lineweight':35 , 'color': 2})

    # get all POLYLINE entities from model space
    #Polyline vertexlerinin yeni listeye alınması
    polylines = msp.query('LWPOLYLINE')
    for polyline in polylines:
        listex=list()
        listey=list()
        a=len(polyline)
        b = 0
        while b<a:
            pl = (polyline.__getitem__(b))
            listex.append(round(pl[0],2))
            listey.append(round(pl[1],2))
            b +=1

    pl0=list(zip(listex,listey))

    #Mevcut Arazinin En küçük y değerinin bulunması
    miny=min(listey)


    for i in pl0:
        if i[1] == miny:
            minx = i[0]


    #Mevcut Arazinin (0,0) Noktasına Taşınması
    listey0 = list()
    listex0 = list()

    for i in listey:
        listey0.append(round((i-miny),2))

    for i in listex:
        listex0.append(round((i-minx),2))

    pl_0=list(zip(listex0,listey0))
    msp1.add_lwpolyline(pl_0,dxfattribs={'layer': 'Arazi'})


    #Yapının Temel koordinatlarının belirlenmesi için mevcut arazinin offsetinin alınması

    listey1=list()
    listex1=list()
    offset = 2

    for i in listey0:
            listey1.append(round((i-offset),2))

    for i in listex0:
            listex1.append(round(i,2))

    pl1=list(zip(listex1,listey1))


    #ENKESİT Çizimleri
    #Eksen Çizimi

    eksenx_0 = 0
    eksenx_1 = 0
    ekseny_0 = -ht
    ekseny_1 = h4+h3+h2+h1+hs
    eksen = [(eksenx_0,ekseny_0-0.2),(eksenx_1,ekseny_1+0.2)]
    msp1.add_lwpolyline(eksen,dxfattribs={'layer': 'Arazi'})

    #Temel
    #Temelin arazi offseti ile kesişen noktalarını bulmak için gerekli fiktif doğru
    plt = ((100,0),(-100,0))

    #Kesişim Noktalarını Belirleme
    l1=LineString(pl1)
    l2=LineString(plt)

    int_pt = l2.intersection(l1)

    #Belirlenen Kesişim Noktalarının 2 haneli yazılması
    psolx=round(int_pt[0].x,0)
    psagx=round(int_pt[1].x,0)

    #Yapı Temel Uzunluğu  ile Savak Uzunkluğu Kontrolü
    hs1 = round(hs,0)
    At = [(-Ls/2-hs1-2,0),(Ls/2+hs1+2,0),(Ls/2+hs1+2,-ht),(-Ls/2-hs1-2,-ht)]
    Bt = [(psolx,0),(psagx,0),(psagx,-ht),(psolx,-ht)]

    if psagx <= Ls/2+hs1+2:
        Plht = At
    else:
        Plht = Bt

    #Yapı Temelinin Çizimi
    plx=msp1.add_lwpolyline(Plht,dxfattribs={'layer': 'Savak'})
    plx.close()

    #1.Kademe
    #Yapının 1.Kademe koordinatlarının belirlenmesi

    #Temelin arazi ile kesişen noktalarını bulmak için gerekli fiktif doğru
    plt1 = ((100,h4),(-100,h4))

    #Kesişim Noktalarını Belirleme
    l11=LineString(pl1)
    l21=LineString(plt1)

    int_pt1 = l21.intersection(l11)

    #Belirlenen Kesişim Noktalarının 2 haneli yazılması
    psolx1=round(int_pt1[0].x,0)
    psagx1=round(int_pt1[1].x,0)

    #Yapı Temel Uzunluğu  ile 1. Kademe Kontrolü

    A1 = [(-Ls/2-hs1-2-1,h4),(Ls/2+hs1+2+1,h4),(Ls/2+hs1+2+1,0),(-Ls/2-hs1-2-1,0)]
    B1 = [(psolx1,h4),(psagx1,h4),(psagx1,0),(psolx1,0)]

    if psagx1 <= (Ls/2+hs1+2+1):
        Plh4 = A1
    else:
        Plh4 = B1

    #Yapı 1.Kademe Çizimi
    plxh4=msp1.add_lwpolyline(Plh4,dxfattribs={'layer': 'Savak'})
    plxh4.close()

    #2.Kademe
    #Yapının 2.Kademe koordinatlarının belirlenmesi

    #Temelin arazi ile kesişen noktalarını bulmak için gerekli fiktif doğru
    plt2 = ((100,h4+h3),(-100,h4+h3))

    #Kesişim Noktalarını Belirleme
    l12=LineString(pl1)
    l22=LineString(plt2)

    int_pt2 = l22.intersection(l12)

    #Belirlenen Kesişim Notlarının 2 haneli yazılması
    psolx2=round(int_pt2[0].x,0)
    psagx2=round(int_pt2[1].x,0)

    #2. Kademe  ile 1. Kademe  Kontrolü

    A2 = [(-Ls/2-hs1-2-1-1,h4+h3),(Ls/2+hs1+2+1+1,h4+h3),(Ls/2+hs1+2+1+1,h4),(-Ls/2-hs1-2-1-1,h4)]
    B2 = [(psolx2,h4+h3),(psagx2,h4+h3),(psagx2,h4),(psolx2,h4)]

    if psagx2 <= (Ls/2+hs1+2+1+1):
        Plh3 = A2
    else:
        Plh3 = B2

    #Yapı 2.Kademe Çizimi

    plxh3=msp1.add_lwpolyline(Plh3,dxfattribs={'layer': 'Savak'})
    plxh3.close()

    #3.Kademe
    #Yapının 3.Kademe koordinatlarının belirlenmesi

    #Kademenin arazi ile kesişen noktalarını bulmak için gerekli fiktif doğru
    plt3 = ((100,h4+h3+h2),(-100,h4+h3+h2))

    #Kesişim Noktalarını Belirleme
    l13=LineString(pl1)
    l23=LineString(plt3)

    int_pt3 = l23.intersection(l13)

    #Belirlenen Kesişim Notlarının 2 haneli yazılması
    psolx3=round(int_pt3[0].x,0)
    psagx3=round(int_pt3[1].x,0)


    #3. Kademe  ile 2. Kademe  Kontrolü

    A3 = [(-Ls/2-hs1-2-1-1-1,h4+h3+h2),(Ls/2+hs1+2+1+1+1,h4+h3+h2),(Ls/2+hs1+2+1+1+1,h4+h3),(-Ls/2-hs1-2-1-1-1,h4+h3)]
    B3 = [(psolx3,h4+h3+h2),(psagx3,h4+h3+h2),(psagx3,h4+h3),(psolx3,h4+h3)]

    if psagx3 <= (Ls/2+hs1+2+1+1+1):
        Plh2 = A3
    else:
        Plh2 = B3

    #Yapı 3.Kademe Çizimi

    plxh2=msp1.add_lwpolyline(Plh2,dxfattribs={'layer': 'Savak'})
    plxh2.close()

    #4.Kademe
    #Yapının 4.Kademe koordinatlarının belirlenmesi

    #Kademenin arazi ile kesişen noktalarını bulmak için gerekli fiktif doğru
    plt4 = ((100,h4+h3+h2+h1+hs),(-100,h4+h3+h2+h1+hs))

    #Kesişim Noktalarını Belirleme
    l14=LineString(pl1)
    l24=LineString(plt4)

    int_pt4 = l24.intersection(l14)

    #Belirlenen Kesişim Notlarının 2 haneli yazılması
    psolx4=round(int_pt4[0].x,0)
    psagx4=round(int_pt4[1].x,0)

    #4. Kademe  ile 3. Kademe  Kontrolü

    A4 = [(-Ls/2-hs1-2-1-1-1-1,h4+h3+h2+h1+hs),(-(Ls/2)-hs,h4+h3+h2+h1+hs),(-(Ls/2),h4+h3+h2+h1+hs-hs),
          ((Ls/2),h4+h3+h2+h1+hs-hs),((Ls/2)+hs,h4+h3+h2+h1+hs),(Ls/2+hs+2+1+1+1+1,h4+h3+h2+h1+hs-hs-h1),
          (Ls/2+hs+2+1+1+1+1,h4+h3+h2+h1+hs-hs-h1),(-Ls/2-hs1-2-1-1-1-1,h4+h3+h2+h1+hs-hs-h1)]

    B4 = [(psolx4,h4+h3+h2+h1+hs),(-(Ls/2)-hs,h4+h3+h2+h1+hs),(-(Ls/2),h4+h3+h2+h1+hs-hs),((Ls/2),h4+h3+h2+h1+hs-hs),
          ((Ls/2)+hs,h4+h3+h2+h1+hs),(psagx4,h4+h3+h2+h1+hs),(psagx4,h4+h3+h2+h1+hs-hs-h1),(psolx4,h4+h3+h2+h1+hs-hs-h1)]


    if psagx4 <= (Ls/2+hs+2+1+1+1+1):
        Plh1 = A4
    else:
        Plh1 = B4


    #Yapı 4.Kademe Çizimi

    plxh1=msp1.add_lwpolyline(Plh1,dxfattribs={'layer': 'Savak'})
    plxh1.close()


    #Kot
    #1
    kot1=[(0-(Ls/2),0), (-0.1-(Ls/2), 0.1), (0.1-(Ls/2), 0.1)]
    kotline = msp1.add_lwpolyline(kot1,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot1 = msp1.add_hatch(color=6)
    hatchkot1.paths.add_polyline_path(kot1,is_closed=1)

    mtext1 = msp1.add_mtext("{}".format(kot), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext1.dxf.char_height = 0.15
    mtext1.set_location((-0.35-(Ls/2),0.35))

    #2
    kot2=[(a1-(Ls/2),h4), (a1-0.1-(Ls/2),h4+0.1), (a1+0.1-(Ls/2),h4+0.1)]
    kotline = msp1.add_lwpolyline(kot2,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot2 = msp1.add_hatch(color=6)
    hatchkot2.paths.add_polyline_path(kot2,is_closed=1)

    mtext2 = msp1.add_mtext("{}".format(kot+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext2.dxf.char_height = 0.15
    mtext2.set_location((a1-0.35-(Ls/2),h4+0.35))

    #3
    kot3=[(a1+a2-(Ls/2),h4+h3), (a2+a1-0.1-(Ls/2),h3+h4+0.1), (a2+a1+0.1-(Ls/2),h3+h4+0.1)]
    kotline = msp1.add_lwpolyline(kot3,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot3 = msp1.add_hatch(color=6)
    hatchkot3.paths.add_polyline_path(kot3,is_closed=1)

    mtext3 = msp1.add_mtext("{}".format(kot+h4+h3), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext3.dxf.char_height = 0.15
    mtext3.set_location((a2+a1-0.35-(Ls/2),h3+h4+0.35))

    #4
    kot4=[(a1+a2+a3-(Ls/2),h2+h3+h4), (a3+a2+a1-0.1-(Ls/2),h2+h3+h4+0.1), (a3+a2+a1+0.1-(Ls/2),h2+h3+h4+0.1)]
    kotline = msp1.add_lwpolyline(kot4,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot4 = msp1.add_hatch(color=6)
    hatchkot4.paths.add_polyline_path(kot4,is_closed=1)

    mtext4 = msp1.add_mtext("{}".format(kot+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext4.dxf.char_height = 0.15
    mtext4.set_location((a3+a2+a1-0.35-(Ls/2),h2+h3+h4+0.35))

    #5
    kot5=[(a4+a3+a2+a1-(Ls),hs+h1+h2+h3+h4), (a4+a3+a2+a1-0.1-(Ls),hs+h1+h2+h3+h4+0.1), (a4+a3+a2+a1+0.1-(Ls),hs+h1+h2+h3+h4+0.1)]
    kotline = msp1.add_lwpolyline(kot5,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot5 = msp1.add_hatch(color=6)
    hatchkot5.paths.add_polyline_path(kot5,is_closed=1)

    mtext5 = msp1.add_mtext("{}".format(kot+hs+h1+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext5.dxf.char_height = 0.15
    mtext5.set_location((a4+a3+a2+a1-0.35-(Ls),hs+h1+h2+h3+h4+0.35))

    #6
    kot6=[(a4+a3+a2+a1-(Ls/2),h1+h2+h3+h4), (a4+a3+a2+a1-0.1-(Ls/2),h1+h2+h3+h4+0.1), (a4+a3+a2+a1+0.1-(Ls/2),h1+h2+h3+h4+0.1)]
    kotline = msp1.add_lwpolyline(kot6,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot6 = msp1.add_hatch(color=6)
    hatchkot6.paths.add_polyline_path(kot6,is_closed=1)

    mtext6 = msp1.add_mtext("{}".format(kot+h1+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext6.dxf.char_height = 0.15
    mtext6.set_location((a4+a3+a2+a1-0.35-(Ls/2),h1+h2+h3+h4+0.35))

    #7
    kot7=[(-(Ls/2),0-ht), (-0.1-(Ls/2), 0.1-ht), (0.1-(Ls/2), 0.1-ht)]
    kotline = msp1.add_lwpolyline(kot7,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot7 = msp1.add_hatch(color=6)
    hatchkot7.paths.add_polyline_path(kot7,is_closed=1)

    mtext7 = msp1.add_mtext("{}".format(kot-ht), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext7.dxf.char_height = 0.15
    mtext7.set_location((-0.35-(Ls/2),0.35-ht))

    #Ölçülendirme
    #Üst

    u5=(Polygon(Plh1).bounds)

    dimu1 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1), (h1+h2+h3+h4+hs+1)), p1=(-Ls/2, h1+h2+h3+h4+hs+.5), p2=(Ls/2, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimu2 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1), (h1+h2+h3+h4+hs+1)), p1=(Ls/2, h1+h2+h3+h4+hs+.5), p2=(Ls/2+hs, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })



    dimu3 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1), (h1+h2+h3+h4+hs+1)), p1=(Ls/2+hs, h1+h2+h3+h4+hs+.5), p2=(u5[2], h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimu4 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1), (h1+h2+h3+h4+hs+1)), p1=(-Ls/2, h1+h2+h3+h4+hs+.5), p2=(-Ls/2-hs, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimu5 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1), (h1+h2+h3+h4+hs+1)), p1=(u5[0], h1+h2+h3+h4+hs+.5), p2=(-Ls/2-hs, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimu6 = msp1.add_linear_dim(base=((h1+h2+h3+h4+hs+1.5), (h1+h2+h3+h4+hs+1.5)), p1=(u5[0], h1+h2+h3+h4+hs+1), p2=(u5[2], h1+h2+h3+h4+hs+1),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimu1.render()
    dimu2.render()
    dimu3.render()
    dimu4.render()
    dimu5.render()
    dimu6.render()

    #Alt
    u1 = (Polygon(Plht).bounds)
    u2 = (Polygon(Plh4).bounds)
    u3 = (Polygon(Plh3).bounds)
    u4 = (Polygon(Plh2).bounds)

    dima1 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u1[0], -ht-.5), p2=(u1[2], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima2 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u1[2], -ht-.5), p2=(u2[2], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima3 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u2[2], -ht-.5), p2=(u3[2], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima4 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u3[2], -ht-.5), p2=(u4[2], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima5 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u4[2], -ht-.5), p2=(u5[2], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima6 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u1[0], -ht-.5), p2=(u2[0], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima7 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u2[0], -ht-.5), p2=(u3[0], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima8 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u3[0], -ht-.5), p2=(u4[0], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima9 = msp1.add_linear_dim(base=((-ht-1), (-ht-1)), p1=(u4[0], -ht-.5), p2=(u5[0], -ht-.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima10 = msp1.add_linear_dim(base=((-ht-1.5), (-ht-1.5)), p1=(u5[0], -ht-1), p2=(u5[2], -ht-1),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima1.render()
    dima2.render()
    dima3.render()
    dima4.render()
    dima5.render()
    dima6.render()
    dima7.render()
    dima8.render()
    dima9.render()
    dima10.render()

    #Sol Yan

    dimhs = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, h1+h2+h3+h4+hs), p2=(u5[0]-0.5, h1+h2+h3+h4),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimhs.shift_text(dh=-0.5, dv=0.1)

    dimh1 = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, h1+h2+h3+h4), p2=(u5[0]-0.5, h1+h2+h3),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh1.shift_text(dh=-0.5, dv=0.1)

    dimh2 = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, h1+h2+h3), p2=(u5[0]-0.5, h1+h2),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh2.shift_text(dh=-0.5, dv=0.1)

    dimh3 = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, h1+h2), p2=(u5[0]-0.5, h1),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh3.shift_text(dh=-0.5, dv=0.1)

    dimh4 = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, h1), p2=(u5[0]-0.5, 0),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh4.shift_text(dh=-0.5, dv=0.1)

    dimht = msp1.add_linear_dim(base=(u5[0]-1,u5[0]-1), p1=(u5[0]-0.5, 0), p2=(u5[0]-0.5, -ht),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimht.shift_text(dh=-0.5, dv=0.1)

    dimv = msp1.add_linear_dim(base=(u5[0]-1.5,u5[0]-1.5), p1=(u5[0]-1,h1+h2+h3+h4+hs), p2=(u5[0]-1, -ht),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimv.shift_text(dh=-0.5, dv=0.1)

    dimhs.render()
    dimh1.render()
    dimh2.render()
    dimh3.render()
    dimh4.render()
    dimht.render()
    dimv.render()

    #Drenaj Boruları Çizimi
    Dcap = 600
    msp1.add_circle((0,0.7),radius=(Dcap/2000),dxfattribs={'layer': 'Boru'})
    msp1.add_line((-(Dcap/2000)-0.1,0.7),((Dcap/2000)+0.1,0.7),dxfattribs={'layer': 'Arazi'})
    msp1.add_lwpolyline([(0,0.7),(1.2,0.3),(5,0.3)],dxfattribs={'layer': 'Hatch'})
    mtext1 = msp1.add_mtext("%%c{} HDPE KORUGE BORU".format((Dcap)), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext1.dxf.char_height = 0.15
    mtext1.set_location((1.4,0.5))

    dimdboru = msp1.add_linear_dim(base=(-.5,-.5), p1=(0,0), p2=(0,.7),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimdboru.render()

    #4. Kademe Borular
    dcap=200
    dcap=dcap/1000
    sayac = 0
    adim = 0
    while sayac < (Ls/2)+1:
        sayac += 1
        msp1.add_circle((-Ls/2+adim,h4+h3+h2+h1-1),radius=(dcap/2),dxfattribs={'layer': 'Boru'})
        adim += 2

    #3. Kademe Borular

    sayac = 0
    adim = 1
    while sayac < (Ls/2):
        sayac += 1
        msp1.add_circle((-Ls/2+adim,h4+h3+h2-1),radius=(dcap/2),dxfattribs={'layer': 'Boru'})
        adim += 2

    msp1.add_lwpolyline([(Ls/2,h4+h3+h2+h1-1),(Ls/2+1.2,h4+h3+h2+h1-.6),(Ls/2+5,h4+h3+h2+h1-.6)],dxfattribs={'layer': 'Hatch'})
    mtext1 = msp1.add_mtext("%%c{} HDPE KORUGE BORU".format((dcap*1000)), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext1.dxf.char_height = 0.15
    mtext1.set_location((Ls/2+1.4,h4+h3+h2+h1-.4))

    dimsboruh = msp1.add_linear_dim(base=(h4+h3+h2+h1-0.8,h4+h3+h2+h1-0.8), p1=(Ls/2,h4+h3+h2+h1-1), p2=(Ls/2-2,h4+h3+h2+h1-1),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimsboruv = msp1.add_linear_dim(base=(Ls/2,h4+h3+h2+h1), p1=(Ls/2-0.2,h4+h3+h2+h1), p2=(Ls/2-0.2,h4+h3+h2+h1-1),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimsavak = msp1.add_linear_dim(base=(-Ls/2,h4+h3+h2+h1), p1=(-Ls/2+0.1,h4+h3+h2+h1+hs), p2=(-Ls/2+0.1,h4+h3+h2+h1),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })


    dimsboruh.render()
    dimsboruv.render()
    dimsavak.render()


    #Savak Çizimi
    bx=Polygon(Plh1).bounds
    Bx= [(bx[0],h4+h3+h2+h1+hs),(-Ls/2-hs,h4+h3+h2+h1+hs),(-Ls/2,h4+h3+h2+h1),(Ls/2,h4+h3+h2+h1),(Ls/2+hs,h4+h3+h2+h1+hs),(bx[2],h4+h3+h2+h1+hs)]

    ax=list(ezdxf.math.offset_vertices_2d(Bx,offset=-0.2))
    msp1.add_lwpolyline(ax,dxfattribs={'layer': 'Savak'})



    #Eğim Çizimleri
    msp1.add_lwpolyline([(-Ls/2-hs-0.2,h4+h3+h2+h1+hs-0.2),(-Ls/2-hs-0.2,h4+h3+h2+h1+hs-0.6),(-Ls/2-hs-0.2+.4,h4+h3+h2+h1+hs-0.6)],dxfattribs={'layer': 'Kot'})
    msp1.add_lwpolyline([(+Ls/2+hs+0.2,h4+h3+h2+h1+hs-0.2),(+Ls/2+hs+0.2,h4+h3+h2+h1+hs-0.6),(+Ls/2+hs-.2,h4+h3+h2+h1+hs-0.6)],dxfattribs={'layer': 'Kot'})

    mtextusol = msp1.add_mtext("1", dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'}).set_location((-Ls/2-hs-0.3,h4+h3+h2+h1+hs-0.3))
    mtextasol = msp1.add_mtext("1", dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'}).set_location((-Ls/2-hs,h4+h3+h2+h1+hs-0.7))
    mtextusol.dxf.char_height = 0.15
    mtextasol.dxf.char_height = 0.15

    mtextusag = msp1.add_mtext("1", dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'}).set_location((Ls/2+hs+0.3,h4+h3+h2+h1+hs-0.3))
    mtextasag = msp1.add_mtext("1", dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'}).set_location((Ls/2+hs,h4+h3+h2+h1+hs-0.7))
    mtextusag.dxf.char_height = 0.15
    mtextasag.dxf.char_height = 0.15




    #PLAN Çizimleri



























    doc1.saveas("oku.dxf")



oku(.5,.6,.8,1,2,5,.5,2.5,2,3,1.5,2,.75,1500.40)