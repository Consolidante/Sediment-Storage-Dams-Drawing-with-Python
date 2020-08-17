import ezdxf


def ply(a1,a2,a3,a4,a5,s,a7,ht,h1,h2,h3,h4,hs,kot):
    #generate new file
    doc = ezdxf.new('R2010',setup=True)
    #generate new modelspace
    msp = doc.modelspace()
    #create layers
    doc.layers.new(name='Tersip Bendi', dxfattribs={'linetype': 'CONTINUOUS','lineweight':53 ,'color': 1})
    doc.layers.new(name='Hatch', dxfattribs={'linetype': 'CONTINUOUS', 'color': 8})
    doc.layers.new(name='Kot', dxfattribs={'linetype': 'CONTINUOUS', 'color': 6})
    doc.layers.new(name='Yazı', dxfattribs={'linetype': 'CONTINUOUS', 'color': 2})
    doc.layers.new(name='Savak', dxfattribs={'linetype': 'CONTINUOUS', 'lineweight':40 , 'color': 3})


    global pl

    a6 = (h4+h3+h2+h1+hs)/s

    pl = [(0,-ht),(0,0),(a1,0),(a1,h4),(a1+a2,h4),(a1+a2,h4+h3),(a1+a2+a3,h4+h3),
          (a1+a2+a3,h4+h3+h2),(a1+a2+a3+a4,h4+h3+h2),(a1+a2+a3+a4,h4+h3+h2+h1-0.2),
          (a1+a2+a3+a4+a5+(hs+0.2)/s,h4+h3+h2+h1-0.2),
          (a1+a2+a3+a4+a5+a6,0),(a1+a2+a3+a4+a5+a6+a7,0),(a1+a2+a3+a4+a5+a6+a7,-ht)]

    polyline = msp.add_lwpolyline(pl,dxfattribs={'layer': 'Tersip Bendi'})
    polyline.close()

    #hatch

    hatch = msp.add_hatch(dxfattribs={'layer': 'Hatch'})
    hatch.set_pattern_fill("GRAVEL",color=8,scale=0.05)
    hatch.paths.add_polyline_path(pl, is_closed=1)


    phatil = [(a1+a2+a3+a4,h4+h3+h2+h1),(a1+a2+a3+a4+a5+0.15+hs*0.2,h4+h3+h2+h1),
              (a1+a2+a3+a4+a5+0.15+(hs+0.2)*0.2,h4+h3+h2+h1-0.2),(a1+a2+a3+a4,h4+h3+h2+h1-0.2)]
    polyline1 = msp.add_lwpolyline(phatil,dxfattribs={'layer': 'Tersip Bendi'})
    polyline1.close()

    hatchhatil = msp.add_hatch(dxfattribs={'layer': 'Hatch'})
    hatchhatil.set_pattern_fill("DOTS",color=8,scale=0.04)
    hatchhatil.paths.add_polyline_path(phatil, is_closed=1)


    psavak = [(a1+a2+a3+a4,h4+h3+h2+h1),(a1+a2+a3+a4,h4+h3+h2+h1+hs),
              (a1+a2+a3+a4+a5,h4+h3+h2+h1+hs),(a1+a2+a3+a4+a5+hs/s,h4+h3+h2+h1)]
    polyline2 = msp.add_lwpolyline(psavak,dxfattribs={'layer': 'Savak'})
    polyline2.close()


    #Savak Hatılı Taraması
    t = (a5 / 0.1)
    t = 2*int(t)
    sayac = 0
    while sayac<t:
        sayac +=1
        t -= 1
        if t % 2 == 0:
            p1 = [(a1+a2+a3+a4+(0.1*sayac),h4+h3+h2+h1+hs),(a1+a2+a3+a4+(0.1*sayac),h4+h3+h2+h1)]
            poly1 = msp.add_lwpolyline(p1,dxfattribs={'layer': 'Hatch'})
            poly1.close()
        else:
            p2 = [(a1+a2+a3+a4+(0.1*sayac),h4+h3+h2+h1+hs),(a1+a2+a3+a4+(0.1*sayac),h4+h3+h2+h1+hs/2)]
            poly2 = msp.add_lwpolyline(p2,dxfattribs={'layer': 'Hatch'})
            poly2.close()



    #dimension h
    dima1 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(0, h1+h2+h3+h4+hs+.5), p2=(a1, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima2 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1, h1+h2+h3+h4+hs+.5), p2=(a1+a2, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima3 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1+a2, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima4 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1+a2+a3, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3+a4, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima5 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1+a2+a3+a4, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3+a4+a5, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima6 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1+a2+a3+a4+a5, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3+a4+a5+a6, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dima7 = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+.8), (h1+h2+h3+h4+hs+.8)), p1=(a1+a2+a3+a4+a5+a6, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3+a4+a5+a6+a7, h1+h2+h3+h4+hs+.5),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimh = msp.add_linear_dim(base=((h1+h2+h3+h4+hs+1.5), (h1+h2+h3+h4+hs+1.5)), p1=(0, h1+h2+h3+h4+hs+.5), p2=(a1+a2+a3+a4+a5+a6+a7, h1+h2+h3+h4+hs+.5),override={
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
    dimh.render()

    #dimension v

    dimhs = msp.add_linear_dim(base=((-1), (-0.7)), p1=(-0.5, h1+h2+h3+h4+hs), p2=(-0.5, h1+h2+h3+h4),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimhs.shift_text(dh=-0.5, dv=0.1)

    dimh1 = msp.add_linear_dim(base=((-1), (-.2)), p1=(-0.5, h1+h2+h3+h4), p2=(-0.5, h2+h3+h4),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh1.shift_text(dh=-0.5, dv=0.1)

    dimh2 = msp.add_linear_dim(base=((-1), (-0.7)), p1=(-0.5, h2+h3+h4), p2=(-0.5, h3+h4),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh2.shift_text(dh=-0.5, dv=0.1)

    dimh3 = msp.add_linear_dim(base=((-1), (-0.7)), p1=(-0.5, h3+h4), p2=(-0.5, h4),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh3.shift_text(dh=-0.5, dv=0.1)

    dimh4 = msp.add_linear_dim(base=((-1), (-0.7)), p1=(-0.5, h4), p2=(-0.5, 0),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimh4.shift_text(dh=-0.5, dv=0.1)

    dimht = msp.add_linear_dim(base=((-1), (-0.7)), p1=(-0.5, 0), p2=(-0.5, -ht),angle=-270,override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })
    dimht.shift_text(dh=-0.5, dv=0.1)

    dimv = msp.add_linear_dim(base=((-2), (-1)), p1=(-1, h1+h2+h3+h4+hs), p2=(-1, -ht),angle=-270,override={
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

    #Kot


    #1
    kot1=[(0,0), (-0.1, 0.1), (0.1, 0.1)]
    kotline = msp.add_lwpolyline(kot1,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot1 = msp.add_hatch(color=6)
    hatchkot1.paths.add_polyline_path(kot1,is_closed=1)

    mtext1 = msp.add_mtext("{}".format(kot), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext1.dxf.char_height = 0.15
    mtext1.set_location((-0.35,0.35))

    #2
    kot2=[(a1,h4), (a1-0.1,h4+0.1), (a1+0.1,h4+0.1)]
    kotline = msp.add_lwpolyline(kot2,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot2 = msp.add_hatch(color=6)
    hatchkot2.paths.add_polyline_path(kot2,is_closed=1)

    mtext2 = msp.add_mtext("{}".format(kot+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext2.dxf.char_height = 0.15
    mtext2.set_location((a1-0.35,h4+0.35))

    #3
    kot3=[(a1+a2,h4+h3), (a2+a1-0.1,h3+h4+0.1), (a2+a1+0.1,h3+h4+0.1)]
    kotline = msp.add_lwpolyline(kot3,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot3 = msp.add_hatch(color=6)
    hatchkot3.paths.add_polyline_path(kot3,is_closed=1)

    mtext3 = msp.add_mtext("{}".format(kot+h4+h3), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext3.dxf.char_height = 0.15
    mtext3.set_location((a2+a1-0.35,h3+h4+0.35))

    #4
    kot4=[(a1+a2+a3,h2+h3+h4), (a3+a2+a1-0.1,h2+h3+h4+0.1), (a3+a2+a1+0.1,h2+h3+h4+0.1)]
    kotline = msp.add_lwpolyline(kot4,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot4 = msp.add_hatch(color=6)
    hatchkot4.paths.add_polyline_path(kot4,is_closed=1)

    mtext4 = msp.add_mtext("{}".format(kot+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext4.dxf.char_height = 0.15
    mtext4.set_location((a3+a2+a1-0.35,h2+h3+h4+0.35))

    #5
    kot5=[(a4+a3+a2+a1,hs+h1+h2+h3+h4), (a4+a3+a2+a1-0.1,hs+h1+h2+h3+h4+0.1), (a4+a3+a2+a1+0.1,hs+h1+h2+h3+h4+0.1)]
    kotline = msp.add_lwpolyline(kot5,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot5 = msp.add_hatch(color=6)
    hatchkot5.paths.add_polyline_path(kot5,is_closed=1)

    mtext5 = msp.add_mtext("{}".format(kot+hs+h1+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext5.dxf.char_height = 0.15
    mtext5.set_location((a4+a3+a2+a1-0.35,hs+h1+h2+h3+h4+0.35))

    #6
    kot6=[(a4+a3+a2+a1,h1+h2+h3+h4), (a4+a3+a2+a1-0.1,h1+h2+h3+h4+0.1), (a4+a3+a2+a1+0.1,h1+h2+h3+h4+0.1)]
    kotline = msp.add_lwpolyline(kot6,dxfattribs={'layer': 'Kot'})
    kotline.close()
    hatchkot6 = msp.add_hatch(color=6)
    hatchkot6.paths.add_polyline_path(kot6,is_closed=1)

    mtext6 = msp.add_mtext("{}".format(kot+h1+h2+h3+h4), dxfattribs={'layer': 'Yazı','style': 'OpenSansCondensed-Light'})
    mtext6.dxf.char_height = 0.15
    mtext6.set_location((a4+a3+a2+a1-0.35,h1+h2+h3+h4+0.35))

    #İnsaat Derzi
    #İ.D-1
    L1 = a2+a3+a4+a5+(h1+h2+h3+h4+hs)/s
    ID1 = (L1 - 1)/3

    id1=[(a1,0), (a1+ID1,0), (a1+ID1+0.2,0-0.2), (a1+ID1+0.2+ID1+0.6,0-0.2), (a1+ID1+0.2+ID1+0.6+0.2,0-0.2+0.2),(a1+ID1+0.2+ID1+0.6+0.2+ID1,0-0.2+0.2)]
    plid1 = msp.add_lwpolyline(id1,dxfattribs={'layer': 'Tersip Bendi'})

    dimid1a = msp.add_linear_dim(base=((0.3), (0.3)), p1=(a1, 0.2), p2=(a1+ID1, 0.2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid1b = msp.add_linear_dim(base=((0.3), (0.3)), p1=(a1+ID1, 0.2), p2=(a1+ID1+0.2, 0.2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid1c = msp.add_linear_dim(base=((0.3), (0.3)), p1=(a1+ID1+0.2, 0.2), p2=(a1+ID1+0.2+ID1+0.6, 0.2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid1d = msp.add_linear_dim(base=((0.3), (0.3)), p1=(a1+ID1+0.2+ID1+0.6, 0.2), p2=(a1+ID1+0.2+ID1+0.6+0.2, 0.2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid1e = msp.add_linear_dim(base=((0.3), (0.3)), p1=(a1+ID1+0.2+ID1+0.6+0.2, 0.2), p2=(a1+ID1+0.2+ID1+0.6+0.2+ID1, 0.2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid1a.render()
    dimid1b.render()
    dimid1c.render()
    dimid1d.render()
    dimid1e.render()

#İ.D-2
    L2 = a3+a4+a5+(h1+h2+h3+hs)/s
    ID2 = (L2 - 1)/3

    id2=[(a1+a2,0+h4), (a1+a2+ID2,0+h4), (a1+a2+ID2+0.2,0-0.2+h4), (a1+a2+ID2+0.2+ID2+0.6,0-0.2+h4), (a1+a2+ID2+0.2+ID2+0.6+0.2,0-0.2+0.2+h4),(a1+ID2+a2+0.2+ID2+0.6+0.2+ID2,0-0.2+0.2+h4)]
    plid2 = msp.add_lwpolyline(id2,dxfattribs={'layer': 'Tersip Bendi'})

    dimid2a = msp.add_linear_dim(base=((0.3+h4), (0.3+h4)), p1=(a1+a2, 0.2+h4), p2=(a1+ID2+a2, 0.2+h4),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid2b = msp.add_linear_dim(base=((0.3+h4), (0.3+h4)), p1=(a1+ID2+a2, 0.2+h4), p2=(a1+ID2+a2+0.2, 0.2+h4),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid2c = msp.add_linear_dim(base=((0.3+h4), (0.3+h4)), p1=(a1+a2+ID2+0.2, 0.2+h4), p2=(a1+a2+ID2+0.2+ID2+0.6, 0.2+h4),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid2d = msp.add_linear_dim(base=((0.3+h4), (0.3+h4)), p1=(a1+a2+ID2+0.2+ID2+0.6, 0.2+h4), p2=(a1+a2+ID2+0.2+ID2+0.6+0.2, 0.2+h4),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid2e = msp.add_linear_dim(base=((0.3+h4), (0.3+h4)), p1=(a1+a2+ID2+0.2+ID2+0.6+0.2, 0.2+h4), p2=(a1+a2+ID2+0.2+ID2+0.6+0.2+ID2, 0.2+h4),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid2a.render()
    dimid2b.render()
    dimid2c.render()
    dimid2d.render()
    dimid2e.render()


#İ.D-3
    L3 = a4+a5+(h1+h2+hs)/s
    ID3 = (L3 - 1)/3

    id3=[(a1+a2+a3,0+h4+h3), (a1+a2+a3+ID3,0+h4+h3), (a1+a2+a3+ID3+0.2,0-0.2+h4+h3), (a1+a2+a3+ID3+0.2+ID3+0.6,0-0.2+h4+h3), (a1+a2+a3+ID3+0.2+ID3+0.6+0.2,0-0.2+0.2+h4+h3),(a1+ID3+a2+a3+0.2+ID3+0.6+0.2+ID3,0-0.2+0.2+h4+h3)]
    plid3 = msp.add_lwpolyline(id3,dxfattribs={'layer': 'Tersip Bendi'})

    dimid3a = msp.add_linear_dim(base=((0.3+h4+h3), (0.3+h4+h3)), p1=(a1+a2+a3, 0.2+h4+h3), p2=(a1+ID3+a2+a3, 0.2+h4+h3),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid3b = msp.add_linear_dim(base=((0.3+h4+h3), (0.3+h4+h3)), p1=(a1+ID3+a2+a3, 0.2+h4+h3), p2=(a1+ID3+a2+0.2+a3, 0.2+h4+h3),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid3c = msp.add_linear_dim(base=((0.3+h4+h3), (0.3+h4+h3)), p1=(a1+a2+ID3+0.2+a3, 0.2+h4+h3), p2=(a1+a2+ID3+0.2+ID3+0.6+a3, 0.2+h4+h3),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid3d = msp.add_linear_dim(base=((0.3+h4+h3), (0.3+h4+h3)), p1=(a1+a2+ID3+0.2+ID3+0.6+a3, 0.2+h4+h3), p2=(a1+a2+ID3+0.2+ID3+0.6+0.2+a3, 0.2+h4+h3),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid3e = msp.add_linear_dim(base=((0.3+h4+h3), (0.3+h4+h3)), p1=(a1+a2+ID3+0.2+ID3+0.6+0.2+a3, 0.2+h4+h3), p2=(a1+a2+ID3+0.2+ID3+0.6+0.2+ID3+a3, 0.2+h4+h3),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid3a.render()
    dimid3b.render()
    dimid3c.render()
    dimid3d.render()
    dimid3e.render()

#İ.D-4
    L4 = a5+(h1+hs)/s
    ID4 = (L4 - 1)/3

    id4=[(a1+a2+a3+a4,0+h4+h3+h2), (a1+a2+a3+a4+ID4,0+h4+h3+h2), (a1+a2+a3+a4+ID4+0.2,0-0.2+h4+h3+h2), (a1+a2+a3+a4+ID4+0.2+ID4+0.6,0-0.2+h4+h3+h2), (a1+a2+a3+a4+ID4+0.2+ID4+0.6+0.2,0-0.2+0.2+h4+h3+h2),(a1+ID4+a2+a3+a4+0.2+ID4+0.6+0.2+ID4,0-0.2+0.2+h4+h3+h2)]
    plid4 = msp.add_lwpolyline(id4,dxfattribs={'layer': 'Tersip Bendi'})

    dimid4a = msp.add_linear_dim(base=((0.3+h4+h3+h2), (0.3+h4+h3+h2)), p1=(a1+a2+a3+a4, 0.2+h4+h3+h2), p2=(a1+ID4+a2+a3+a4, 0.2+h4+h3+h2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid4b = msp.add_linear_dim(base=((0.3+h4+h3+h2), (0.3+h4+h3+h2)), p1=(a1+ID4+a2+a3+a4, 0.2+h4+h3+h2), p2=(a1+ID4+a2+0.2+a3+a4, 0.2+h4+h3+h2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid4c = msp.add_linear_dim(base=((0.3+h4+h3+h2), (0.3+h4+h3+h2)), p1=(a1+a2+ID4+0.2+a3+a4, 0.2+h4+h3+h2), p2=(a1+a2+ID4+0.2+ID4+0.6+a3+a4, 0.2+h4+h3+h2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid4d = msp.add_linear_dim(base=((0.3+h4+h3+h2), (0.3+h4+h3+h2)), p1=(a1+a2+ID4+0.2+ID4+0.6+a3+a4, 0.2+h4+h3+h2), p2=(a1+a2+ID4+0.2+ID4+0.6+0.2+a3+a4, 0.2+h4+h3+h2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid4e = msp.add_linear_dim(base=((0.3+h4+h3+h2), (0.3+h4+h3+h2)), p1=(a1+a2+ID4+0.2+ID4+0.6+0.2+a3+a4, 0.2+h4+h3+h2), p2=(a1+a2+ID4+0.2+ID4+0.6+0.2+ID4+a3+a4, 0.2+h4+h3+h2),override={
        'dimtsz': 0,  # set tick size to 0 to enable arrow usage
        'dimasz': 0.25,  # arrow size in drawing units
        'dimblk': "OBLIQUE",  # arrow block name
        'dimexe': 0.1,
        'dimclrt': 2,
        'dimclrd': 9
    })

    dimid4a.render()
    dimid4b.render()
    dimid4c.render()
    dimid4d.render()
    dimid4e.render()





    #save
    doc.saveas("a.dxf")


ply(.5,.6,.8,1,2,5,.5,2.5,2,3,1.5,2,.75,1500.40)




