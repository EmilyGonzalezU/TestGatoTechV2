from django.urls import path
from . import views


urlpatterns = [
        path('home/', views.index, name='home'),
        path('pc/', views.general_pc, name='general_pc'),
        path('pc gamer/', views.general_pc_gamer, name="pc_gamer"),
        path('pc escritorio/', views.general_pc_escritorio, name="pc_escritorio"),
        path('procesadores/', views.general_processors, name='general_processors'),
        path('procesadores_amd/', views.general_proce_amd, name='general_proce_amd'),
        path('procesadores_intel/', views.general_proce_intel, name='general_proce_intel'),        
        path('placa_madre/', views.general_placa, name='general_placa'),
        path('placa_madre_amd/', views.general_placa_amd, name='general_placa_amd'),
        path('placa_madre_intel/', views.general_placa_intel, name='general_placa_intel'),
        path('ram/', views.general_ram, name='general_ram'),
        path('almacenamiento/', views.general_almacenamiento, name='general_almacenamiento'),
        path('almacenamiento_hdd/', views.general_hdd, name='general_hdd'),
        path('almacenamiento_ssd/', views.general_ssd, name='general_ssd'),
        path('almacenamiento_nvme/', views.general_nvme, name='general_nvme'),
        path('fuente_de_poder/', views.general_fP, name='general_fP'),
        path('tarjeta_grafica/', views.general_gpu, name='general_gpu'),
        path('tarjeta_grafica_amd/', views.general_gpu_amd, name='general_gpu_amd'),
        path('tarjeta_grafica_intel/', views.general_gpu_intel, name='general_gpu_intel'),
        path('tarjeta_grafica_nvidia/', views.general_gpu_nvidia, name='general_gpu_nvidia'),
        path('gabinete/', views.general_gabinete, name='general_gabinete'), 
        path('notebook/', views.general_notebooks, name='general_notebooks'),
        path('notebook gamer/', views.general_note_gamer, name='general_note_gamer'),
        path('notebook oficina/', views.general_note_escritorio, name='general_note_escritorio'),
        path('mouse/', views.general_mouse, name='general_mouse'),
        path('mouse_optico/', views.general_mouse_optico, name='general_mouse_optico'),
        path('mouse_laser/', views.general_mouse_laser, name='general_mouse_laser'),
        path('teclados/', views.general_keyboard, name='general_keyboard'),
        path('teclados_mecanicos/', views.general_mecanico, name='general_mecanico'),
        path('teclados_membrana/', views.general_membrana, name='general_membrana'),
        path('audifonos/', views.general_headset, name='general_headset'),
        path('audifonos_headset/', views.general_headset_headset, name='general_headset_headset'),
        path('monitores/', views.general_monitor, name='general_monitor'),
        path('productos/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
        path('suge/', views.products, name='products'),


] 

