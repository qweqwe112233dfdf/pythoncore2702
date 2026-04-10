from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()

choices_map = {
    '1': 'камінь'
    '2': 'ножиці'
    '3': 'папір'
}
def show_menu():
    panel = Panel(
        "[ 1 ] Почати гру\n[ 2 ] Історія ігор\n[ 3 ] Вихід",
    )
    console.print(panel)
def get_result(player,computer):
    if player == computer:
        return 'нічия'
    elif(
        (player == 'камінь' and computer == 'ножиці' or
        (player == 'ножиці' and computer == 'папір') or
        (player == 'папір' and computer == 'камінь')
    ):
        return 'перемога'
    else:
        return 'поразка'

def play_game():
    player_choice = Prompt.ask(
        'оберіть: [1] камінь, [2] ножиці [3] папір',
        choices=['1','2','3']
    )
    player = choices_map[player_choice]
    computer = random.choice(list(choices_map.values()))

    result = get_result(player,computer)

    if result == 'перемога':
        console.print('ви перемогли!')
    elif result == 'поразка':
        console.print('ви програли!')
    else:
        console.print('нічия!')

    history.append ({
        'player': player
        'computer': computer
        'result': result
    })

def show_history():
    if not history:
        console.print('історія порожня!')
        return

table = Table(title = 'історія ігор')
table.add_column('раунд')
table.add_column('гравець')
table.add_column("комп'ютер")
table.add_column('результат')

wins = losses = draws = 0

for i, game in enumerate(history, start = 1):
    table.add_row(
        str(i)
        game['player']
        game['computer']
        game['result']
    )
    if game['result'] == 'перемога':
        wins += 1
    elif game['result'] == 'поразка':
        losses += 1
    else:   
        draws += 1
console.print(table)

console.print(
    f'\n[bold]статистика:[/bold] '
    f'[green]перемоги: {wins}[/green], '
    f'[red]поразки: {losses}[/red] '
    f'[yellow]ничії: {draws}[/yellow]'
)

while True:
    show_menu()

    choice = Prompt.ask(
        'ваш вибір'
        choices=['1', '2', '3']
    )

    if choice == '1':
        play_game()
    elif choice == '2':
        show_history()
    elif choice == '3':
        console.print('exit')
        break