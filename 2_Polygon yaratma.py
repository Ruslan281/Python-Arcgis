import arcpy
from time import sleep
arcpy.env.workspace=r'C:\Users\KTB\Desktop' #workspace teyin edirik
print"Aktiv edildi"
sleep(2)

print"GDB icersindeki Noqte(feature_class)-i Line-a ceviririk"

arcpy.PointsToLine_management('Noqte',
                              r'C:\Users\KTB\Desktop\Ruslann.gdb\Noqte_Line',
                              '#', '#', 'CLOSE')
# '#' line fieldi bildirir bos oldgu ucun
# '#' sort fieldi fildiir

sleep(2)
print"Line Noqte_Line yaradildi"

sleep(2)

print"GDB icerisinde Noqte_Line vasitesile Polygon ve adini Parsel qoyuruq cekirik"

sleep(2)

arcpy.FeatureToPolygon_management('Noqte_Line',
                                  r'C:\Users\KTB\Desktop\Ruslann.gdb\Parsel',
                                  '#', 'ATTRIBUTES', '#')

# '#' isareti toleransligi bildirir
# 'Attributes' preserves atribut yeni atributlari qoruma altina almaq
# 'Label featureni bildirir.secimde ede bilerik
sleep(2)
print"Adi Parsel olan Paliqonumuz yaradildi"

sleep(2)
print"Bu Parsel uzerine 'Buffer verilir' "

arcpy.Buffer_analysis('Parsel',
                      r'C:\Users\KTB\Desktop\Ruslann.gdb\Parsel_Buffer',
                      '10 Meters', 'FULL', 'ROUND', 'NONE', '#')


sleep(2)

print"Parsel Buffer yaradildi(10 metir)"

sleep(2)

print"""Yaradilmis Paliqon icerisinde yeniden ixtiyari
Paliqon yaratmaq ucun movcud Paliqon icerisinde random
4 eded noqte emele getiririk"""
sleep(2)
arcpy.CreateRandomPoints_management(r'C:\Users\KTB\Desktop\Ruslann.gdb',
                                    'Random_Noqte', 'Parsel', '0 0 250 250',
                                    '5', '0 Meters', 'MULTIPOINT', '2')



# {out name}-Ad cixisi- Random Noqte
# {constraining_feature_class}-Hansi feature classda yaradilacagini teyin edirik.Biz Parsel secirik
# {constraining_extent}-Constakt effektlerini bildirir avtomatik olaraq teyin edirik.(Left,Right,bottom)
# {number_of_points_or_field}-Noqtenin uzunlugunu teyin edirik ve nece eded olacagini (4)
# {minimum_allowed_distance}-Minimum mesafe daxil edirik.Standart olaraq 0 Metir teyin edirik
# {create_multipoint_output}-Bu isareni aktiv edirik.Noqteni poliqon icerisinde random olaraq yerlesdirmek ucun
# {multipoint_size}-Noqtelerin olcusunu bildirir.2 olaraq teyin edirik
sleep(2)
print"""Bu noqtelerden Poligon yaratmaq ucun
evvelce bu noqteleri (Multipart) yeni partlatmaq lazimdir.
Sonra bu noqteleri evvelki kimi line cevirmek lazimdir.
Daha sonra ise (line_to_polygon)deyerek Poligona cevirmek lazimdir"""


arcpy.MultipartToSinglepart_management('Random_Noqte',
                                       r'C:\Users\KTB\Desktop\Ruslann.gdb\Partladilmis_Noqteler')

sleep(2)
print"Random noqteler ugurla Multipart edildi"
sleep(2)
print"Partladilmis noqteleri Line -a cevirek"

arcpy.PointsToLine_management('Partladilmis_Noqteler',
                              r'C:\Users\KTB\Desktop\Ruslann.gdb\Partladilmis_Noqteler_Line',
                              '#', '#', 'CLOSE')
sleep(2)
print"Parladilmis Noqteler ugurla Line-a cevrildi"
sleep(2)
print"Line -i Polygona cevirib ixtiyari Poliqonu elde edek"


arcpy.FeatureToPolygon_management('Partladilmis_Noqteler_Line',
                                  r'C:\Users\KTB\Desktop\Ruslann.gdb\Parsel_1',
                                  '#', 'ATTRIBUTES', '#')
sleep(2)
print"Line Poliqona cevrildi"

sleep(2)


arcpy.Clip_analysis('Parsel_1', 'Parsel',
                    r'C:\Users\KTB\Desktop\Ruslann.gdb\Parsel_Clip', '#')

sleep(2)
print"Clipleme islemi yerine yetrildi"

sleep(2)
print"""GDB icerisinde (Parsel,Parsel_1,Parsel_Clip,Parsel_Buffer,Noqte)-den
basqa elave yaradilmis komekci parametrleri silek"""

sleep(2)
arcpy.Delete_management(r'C:\Users\KTB\Desktop\Ruslann.gdb\Noqte_Line','FeatureClass')

arcpy.Delete_management(r'C:\Users\KTB\Desktop\Ruslann.gdb\Partladilmis_Noqteler','FeatureClass')

arcpy.Delete_management(r'C:\Users\KTB\Desktop\Ruslann.gdb\Partladilmis_Noqteler_Line','FeatureClass')

arcpy.Delete_management(r'C:\Users\KTB\Desktop\Ruslann.gdb\Random_Noqte','FeatureClass')
sleep(2)
print"Silinme emeliyyatli ugurla yerine yetrildi"

sleep(2)

arcpy.Compact_management(r'C:\Users\KTB\Desktop\Ruslann.gdb')
sleep(2)
print"GDB-ye Compact verilib hazir veziyyete getirildi"



















































