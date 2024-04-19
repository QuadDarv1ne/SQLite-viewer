import flet as ft

def main(page: ft.Page):
    page.title = "SQLite Viewer"

    plH1 = ft.CupertinoTextField(
            placeholder_text="users",
            bgcolor=ft.colors.WHITE24,
            )
    def close_dlg(dialog):
        dialog.open = False
        page.update()

    def create_table(e):
        table_name = plH1.value
        close_dlg(CreateTableDialog)
        return table_name

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
    def open_create_table_dialog(e):
        page.dialog = CreateTableDialog
        CreateTableDialog.open = True
        page.update()
    
    CreateTableButton = ft.ElevatedButton(text="Создать таблицу", on_click=open_create_table_dialog)
    AddColumnButton = ft.ElevatedButton(text="Добавить столбец")
    page.add(
        ft.Row(
            [
                CreateTableButton,
                AddColumnButton,
            ]
        ),
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        ),
    )

ft.app(target=main)
