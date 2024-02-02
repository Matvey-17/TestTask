# TestTask
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:  
🔸Меню реализовано через template tag.  
🔸Все, что над выделенным пунктом – развернуто.  
🔸Первый уровень вложенности под выделенным пунктом тоже развернут.  
🔸Хранится в БД.  
🔸Редактируется в стандартной админке Django.  
🔸Активный пункт меню определяется исходя из URL текущей страницы.  
🔸Меню на одной странице может быть несколько. Они определяются по названию.  
🔸При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.  
🔸На отрисовку каждого меню требуется ровно 1 запрос к БД.
   
django-app должен позволять вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
  
❗При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.