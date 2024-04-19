import flet as ft
import sql_commands as sq

def main(page: ft.Page):
    #Инициализация
    page.title = "SQLite Viewer"
    selected_db = ft.Text()
    columns = []
    rows = []
    
    global dbPATH
    # plH1 = ft.CupertinoTextField(
    #         placeholder_text="users",
    #         bgcolor=ft.colors.WHITE24,
    # )
    


    def pick_db_result(e: ft.FilePickerResultEvent):
        
        selected_db.value = e.files[0].path if e.files else None
        dbPATH = selected_db.value
        
        if dbPATH:
            columns = list(map(lambda x: ft.DataColumn(ft.Text(x)), sq.get_columns(dbPATH)))
            rows = list(map(lambda x: ft.DataRow(cells=list(map(lambda y: ft.DataCell(ft.TextField(y, border=ft.InputBorder.NONE, on_submit=cell_changed)), x))), sq.get_rows(dbPATH)))
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
            page.add(dbTable)
            page.update()
    
    def cell_changed(e):
        print([[j.content.value for j in i.cells] for i in dbTable.rows])
    pick_db_dialog = ft.FilePicker(on_result=pick_db_result)
    page.overlay.append(pick_db_dialog)

    




    # #Функция для закрытия диалога
    # def close_dlg(dialog):
    #     dialog.open = False
    #     page.update()

    #Функция для создания таблицы
    # def create_table(e):
    #     table_name = plH1.value
    #     close_dlg(CreateTableDialog)

    #Диалог для создания таблицы
    # CreateTableDialog = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text("Название таблицы:"),
    #     content=plH1,
    #     actions=[
    #         ft.TextButton("Отмена", on_click=lambda e: close_dlg(CreateTableDialog)),
    #         ft.TextButton("ОК", on_click=create_table),
    #     ],
    #     actions_alignment=ft.MainAxisAlignment.END,
    #     on_dismiss=lambda e: print("Create table dialog was dismissed!"),
    # )

    #Функция для открытия диалога
    # def open_create_table_dialog(e):
    #     page.dialog = CreateTableDialog
    #     CreateTableDialog.open = True
    #     page.update()
    
    #Функция для импорта базы данных
    
    
    #Кнопки
    # CreateTableButton = ft.ElevatedButton(icon=ft.icons.TABLE_VIEW, text="Создать таблицу", on_click=open_create_table_dialog)
    AddColumnButton = ft.ElevatedButton(icon=ft.icons.VIEW_COLUMN, text="Добавить столбец")
    ImportDBButton = ft.ElevatedButton(icon=ft.icons.UPLOAD_FILE, text="Импорт", on_click=(lambda _: pick_db_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=["db"],
        )))

        
    #Основная страница
    page.add(

        #Строка меню
        ft.Row(
            [
                ImportDBButton,
                # CreateTableButton,
                AddColumnButton,
            ]
        ),
    )
ft.app(target=main)
