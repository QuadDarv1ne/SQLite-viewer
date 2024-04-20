import flet as ft
import sql_commands as sq

def main(page: ft.Page):
    #Инициализация
    page.title = "SQLite Viewer"
    selected_db = ft.Text()
    global dbTable
    global addFIELDS
    addFIELDS = []
    dbTable = ft.DataTable()
    page.add(dbTable)
    


    def pick_db_result(e: ft.FilePickerResultEvent):   
        selected_db.value = e.files[0].path if e.files else None
        global dbPATH
        dbPATH = selected_db.value if selected_db.value else dbPATH
        load_data(dbPATH) if dbPATH else None
            
    
    def del_row(e):
        #print(e.control.data)
        sq.del_row(dbPATH, e.control.data, sq.get_columns(dbPATH))
    def load_data(dbpath):
        columns = list(map(lambda x: ft.DataColumn(ft.Text(x)), sq.get_columns(dbPATH)))
        columns.append(ft.DataColumn(ft.Text("Действия")))
        rows = []
        for row in sq.get_rows(dbPATH):
            n = ft.DataRow()
            for cell in row:
                n.cells.append(ft.DataCell(ft.Text(cell)))
            n.cells.append(ft.DataCell(ft.IconButton(ft.icons.DELETE, data=row, icon_color="red", on_click=del_row)))
            rows.append(n)
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
        #page.update()


    def close_dlg(e):
        add_row_alert.content.clean()
        add_row_alert.open = False
        page.update()
    
    def update_table_with_new_row(e):
        sq.add_row(dbPATH, tuple([i.value for i in addFIELDS]))
        close_dlg(e)
        #load_data(dbPATH)
        
    
    add_row_alert = ft.AlertDialog(
            modal=True,
            title=ft.Text("Добавление записи"),
            actions=[
                ft.ElevatedButton(
                    icon=ft.icons.CLOSE,
                    text="Отмена",
                    on_click=close_dlg,
                ),
                ft.ElevatedButton(
                    icon=ft.icons.ADD,
                    text="Добавить",
                    on_click=update_table_with_new_row,
                )
            ]
        )
    
    def add_row(e):
        for i in sq.get_columns(dbPATH):
            addFIELDS.append(ft.TextField(label=i))
        add_row_alert.content = ft.Column(addFIELDS)
        #add_row_alert.content = ft.Column([ft.TextField(label=i) for i in sq.get_columns(dbPATH)])
        page.dialog = add_row_alert
        add_row_alert.open = True
        page.update()
    
    
    

    pick_db_dialog = ft.FilePicker(on_result=pick_db_result)
    page.overlay.append(pick_db_dialog)
    
    
    #Кнопки
    AddColumnButton = ft.ElevatedButton(icon=ft.icons.ADD, text="Добавить запись", on_click=add_row, disabled=True)
    ImportDBButton = ft.ElevatedButton(icon=ft.icons.UPLOAD_FILE,
                                       text="Импорт",
                                       on_click=(lambda _: pick_db_dialog.pick_files(
                                                 allow_multiple=False,
                                                 allowed_extensions=["db"],
                                                )))
    UpdateTableButton = ft.ElevatedButton(icon=ft.icons.UPDATE, text="Обновить таблицу", on_click=load_data)
    menu = ft.Row(
            [
                ImportDBButton,
                AddColumnButton,
                UpdateTableButton
            ]
            )
  
    #Основная страница
    page.add(menu)
ft.app(target=main)
