from django.core.management import BaseCommand
from main.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            Category(name="Одежда", description="Одежда разных размеров и цветов."),
            Category(name="Настольные игры", description="Различные настольные игры для веселых посиделок."),
            Category(name="Видеоигры", description="Видеогры любых жанров и тематик."),
            Category(name="Книги", description="Книги разных жанров и авторов."),
        ]
        Category.objects.bulk_create(categories)

        products = [
            Product(name="Футболка", description="Футболка с лого BG3", image='bg3_logo.png', category=categories[0],
                    price=9.99),
            Product(name="Pathfinder",
                    description="«Pathfinder: Настольная ролевая игра. "
                                "Стартовый набор» содержит всё необходимое, чтобы провести настольную ролевую игру "
                                "в жанре фэнтези для компании из 2–5 участников.", image='pathfinder.png',
                    category=categories[1], price=19.99),
            Product(name="Dungeons and Dragons", description="Спускайтесь в древние подземные лабиринты, охотьтесь "
                                                             "за несметными сокровищами, сражайтесь с легендарными "
                                                             "монстрами!", image='dnd.png', category=categories[1],
                    price=24.99),
            Product(name="Baldur’s Gate 3", description="Компьютерная ролевая игра, разработанная и изданная "
                                                        "бельгийской компанией Larian Studios. Baldur’s Gate 3 стала "
                                                        "продолжением серии Baldur’s Gate, основанной на настольной "
                                                        "ролевой игре Dungeons & Dragons;", image='bg3_ps5.png',
                    category=categories[2],
                    price=59.99),
            Product(name="Divinity: Original Sin II", description="партийная компьютерная ролевая игра, сиквел "
                                                                  "Divinity: Original Sin, с однопользовательским и "
                                                                  "многопользовательским режимами игры, разработанная "
                                                                  "компанией Larian Studios на средства, полученные с "
                                                                  "пожертвований с Kickstarter.", image='dos_2_ps4.png',
                    category=categories[2], price=49.99),
            Product(name="Dungeons & Dragons. Книга игрока", description="Dungeons & Dragons. Книга игрока – это самый "
                                                                         "необходимый инструмент для любого игрока, "
                                                                         "который собирается отправиться покорять "
                                                                         "пространства подземелий и драконов. В книге "
                                                                         "вы найдёте все необходимые правила для "
                                                                         "создания собственного уникального персонажа "
                                                                         "и его дальнейшего развития.",
                    image='dnd_player_book.png',
                    category=categories[3], price=14.99),

        ]
        Product.objects.bulk_create(products)
