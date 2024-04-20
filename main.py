import flet as ft
import sql_commands as sq

def main(page: ft.Page):
    #Инициализация
    page.title = "SQLite Viewer"
    selected_db = ft.Text()
    global dbTable
    dbTable = ft.DataTable()
    page.add(dbTable)
    


    def pick_db_result(e: ft.FilePickerResultEvent):   
        selected_db.value = e.files[0].path if e.files else None
        global dbPATH
        dbPATH = selected_db.value if selected_db.value else dbPATH
        load_data(dbPATH) if dbPATH else None
            
    
    def load_data(dbpath):
        columns = list(map(lambda x: ft.DataColumn(ft.Text(x)), sq.get_columns(dbPATH)))
        rows = list(map(lambda x: ft.DataRow(cells=list(map(lambda y: ft.DataCell(ft.Text(y)), x))), sq.get_rows(dbPATH)))
        global dbTable
        dbTable = ft.DataTable(
                                show_checkbox_column=True,
                                column_spacing=200,
                                vertical_lines=ft.border.BorderSide(1, "white"),
                                border=ft.border.all(2, "white"),
                                border_radius=10,
                                columns=columns,
                                rows=rows,
                                )
        AddColumnButton.disabled = False
        page.clean()
        page.add(menu)
        page.add(dbTable)
        page.update()
        
    def add_row(e):
        for i in sq.get_columns(dbPATH):
            page.add(ft.TextField(label=i))
    




    pick_db_dialog = ft.FilePicker(on_result=pick_db_result)
    page.overlay.append(pick_db_dialog)
    
    
    #Кнопки
    AddColumnButton = ft.ElevatedButton(icon=ft.icons.ADD, text="Добавить запись", on_click=add_row, disabled=True)
    ImportDBButton = ft.ElevatedButton(icon=ft.icons.UPLOAD_FILE, text="Импорт", on_click=(lambda _: pick_db_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=["db"],
        )))
    menu = ft.Row(
            [
                ImportDBButton,
                AddColumnButton,
            ]
            )
  
    #Основная страница
    page.add(menu)
ft.app(target=main)
