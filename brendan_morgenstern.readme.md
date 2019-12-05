Implemented features:
- Add appointments
- Record appointments (date, time, duration, location, name, notes) to database
- Automatically refresh view when filtering or editing/adding/deleting appointments

Files changed:
brendan_morgenstern.readme.md
app/models.py
app/main/forms.py
app/main/routes.py
app/templates/main/todolist.html
app/templates/main/todolist.old.html
app/templates/main/todolist_edit_view.html
app/templates/main/todolist_edit_view.old.html

Features not yet implemented:
- Delete appointments
- View current day appointments
- View current week appointments
- Filter appointments by overdue status
- Filter appointments by completed status
- Filter by both overdue and completed status at the same time
- Filter by client name
- Filter by location/notes/other text
- Edit appointments (pop up with notes and editiing widgets)
