import arcpy  # arcpy modulunu idxal edirik programa
from time import sleep

arcpy.env.workspace=r'C:\Users\KTB\Desktop'  # workspace teyin edirik
print "Isleme alani aktiv edildi"
sleep(2)
print "Masaustunde yeni bir 'GDB' yaradilir......."
sleep(2)

arcpy.CreateFileGDB_management(r'C:\Users\KTB\Desktop', 'Ruslann', 'CURRENT')  # Masaustunde yeni GDB fayli yaradiriq.Current gdb novu
sleep(2)
print "Masaustunde yeni bir 'GDB' yaradildi"
sleep(2)
print "GDB icerisinde 'Noqte(Point) 1 eded feature_class elave edirik"

arcpy.CreateFeatureclass_management(r'C:\Users\KTB\Desktop\Ruslann.gdb',
                                    'Noqte', 'POINT', '#', 'DISABLED',
                                    'DISABLED',
                                    """PROJCS['WGS_1984_UTM_Zone_38N',
GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],
PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',45.0],
PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],
UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0,001;0,001;0,
001;IsHighPrecision""", '#', '0', '0', '0')

sleep(2)
print "Noqte(Feature_class) GDB icerisine elave edildi"
