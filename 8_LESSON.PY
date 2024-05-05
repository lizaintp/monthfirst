import random
random.randint(1,3)

import main #импорт модуля
main.asn(2,4)
main.sub(2,4)

from main import sub , asn  #точечный импорт

sub(2,4)
asn(2,4)

from main import * #из модуля импорт
sub(13,3)
asn(2,3)
#встроенный , кастомный, внешние (библиотеки) модули