class Create_person(LoginRequiredMixin, View):

    def get(self, request):
        form = create_personForm()
        return render(request, 'Person/create_person.html', {'form': form})

    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
#            form.instance.creating_date = datetime.now()
            form.clean()
            try:
                data = form.save()
            except:
                return render(request, 'Person/create_person.html', {'form': form})
            else:
                success = 'Кандидат внесен в базу'
        else:
            success = 'Некорректные данные'
            render(request, 'Person/create_person.html', {
                'form': form, 'success': success })
        pk = data.id
        return reverse('detail_person', kwargs={"pk": pk})
