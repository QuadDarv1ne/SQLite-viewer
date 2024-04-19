import flet as ft
import sql_commands as sq

def main(page: ft.Page):

    
    def pick_db_result(e: ft.FilePickerResultEvent):
        selected_db.value = e.files[0].path
        print(selected_db.value)
    #Инициализация
    page.title = "SQLite Viewer"
    
    global dbPATH
    plH1 = ft.CupertinoTextField(
            placeholder_text="users",
            bgcolor=ft.colors.WHITE24,
    )
    dbTable = ft.DataTable()
    

    pick_db_dialog = ft.FilePicker(on_result=pick_db_result)
    selected_db = ft.Text()
    page.overlay.append(pick_db_dialog)

    def import_db(e):
        pick_db_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=["db"],
        )


    #Функция для закрытия диалога
    def close_dlg(dialog):
        dialog.open = False
        page.update()

    #Функция для создания таблицы
    def create_table(e):
        table_name = plH1.value
        close_dlg(CreateTableDialog)

    #Диалог для создания таблицы
    CreateTableDialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Название таблицы:"),
        content=plH1,
        actions=[
            ft.TextButton("Отмена", on_click=lambda e: close_dlg(CreateTableDialog)),
            ft.TextButton("ОК", on_click=create_table),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Create table dialog was dismissed!"),
    )

    #Функция для открытия диалога
    def open_create_table_dialog(e):
        page.dialog = CreateTableDialog
        CreateTableDialog.open = True
        page.update()
    
    #Функция для импорта базы данных
    
    
    #Кнопки
    CreateTableButton = ft.ElevatedButton(icon=ft.icons.TABLE_VIEW, text="Создать таблицу", on_click=open_create_table_dialog)
    AddColumnButton = ft.ElevatedButton(icon=ft.icons.VIEW_COLUMN, text="Добавить столбец")
    ImportDBButton = ft.ElevatedButton(icon=ft.icons.UPLOAD_FILE, text="Импорт", on_click=import_db)

        
    #Основная страница
    page.add(

        #Строка меню
        ft.Row(
            [
                ImportDBButton,
                CreateTableButton,
                AddColumnButton,
            ]
        ),
        #Таблица базы данных
        dbTable,
    )

ft.app(target=main)
