from django.shortcuts import render, redirect
from django.contrib import messages
from .models import miembro, nacionalidad, estadocivil, genero

def agregar_miembro(request):
    nacionalidades = nacionalidad.objects.all()
    estadociviles = estadocivil.objects.all()
    generos = genero.objects.all()

    if request.method == 'POST':
        data = request.POST
        nombre = data['nombre']
        apellido = data['apellidos']
        nacionalidad_id = data['nacionalidad']
        estadocivil_id = data['estadocivil']
        genero_id = data['genero']
        di = data['id']
        direccion = data['direccion']
        telefono = data['telefono']
        correo = data['correo']
        nohijos = data['num_hijos']

        try:
            nacionalidad_obj = nacionalidad.objects.get(pk=nacionalidad_id)
            estadocivil_obj = estadocivil.objects.get(pk=estadocivil_id)
            genero_obj = genero.objects.get(pk=genero_id)

            nuevo_miembro = miembro(
                nombre=nombre,
                apellido=apellido,
                nacionalidad=nacionalidad_obj,
                estadocivil=estadocivil_obj,
                genero=genero_obj,
                di=di,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
                nohijos=nohijos
            )
            nuevo_miembro.save()

            messages.success(request, 'Miembro creado con éxito!', extra_tags="success")
            return redirect('listar_miembros')

        except Exception as e:
            messages.error(request, 'Error al crear el miembro: ' + str(e), extra_tags="danger")
            return redirect('agregar_miembro')

    return render(request, "miembro/miembros.html", {'nacionalidades': nacionalidades, 'estadosciviles': estadociviles, 'generos': generos})

def listar_miembros(request):
   
    miembros = miembro.objects.all()

    return render(request, "miembro/listar_miembros.html", {'miembros': miembros})

'''
def suppliersAddView(request):
    context = {
        "active_icon": "suppliers",
    }
    if request.method == 'POST':
        data = request.POST
        attributes = {
            "first_name": data['first_name'],
            "company_name": data['company_name'],
            "address": data['address'],
            "email": data['email'],
            "phone": data['phone'],
            "assessment": data['rating'],
        }
        if Supplier.objects.filter(**attributes).exists():
            messages.error(request, '¡El proveedor ya existe!',
                extra_tags="warning")
            return redirect('Apps.suppliers:suppliers_add')
        try:
            new_suppliers = Supplier.objects.create(**attributes)
            new_suppliers.save()
            messages.success(request, '¡Proveedor: ' + attributes["first_name"] + " " +
                attributes["company_name"] + ' Creado con éxito!', extra_tags="success")
            return redirect('Apps.suppliers:suppliers_list')
        except Exception as e:
            messages.success(
                request, '¡Hubo un error durante la creación!'+ str(e), extra_tags="danger")
            return redirect('Apps.suppliers:suppliers_add')
    return render(request, "suppliers/suppliers_add.html", context=context)





def suppliersListView(request):
    context = {
        "active_icon": "suppliers",
        "suppliers": Supplier.objects.all()
    }
    return render(request, "suppliers/suppliers.html", context=context)
'''