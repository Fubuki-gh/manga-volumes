from enum import Enum

class Language(Enum):
    # Präfix 978
    ENGLISH     = 0     # Englisch (Australien, Großbritannien, Irland, Kanada, Neuseeland, Puerto Rico, Simbabwe, Südafrika, USA)
    FRENCH      = 2     # Französisch (Belgien, Frankreich, Kanada, Luxemburg, französischsprachige Schweiz)
    GERMAN      = 3     # Deutsch (Deutschland, deutschsprachiges Belgien, Liechtenstein, Österreich, deutschsprachige Schweiz, ehemalige DDR)
    JAPANESE    = 4     # Japanisch
    RUSSIAN     = 5     # Russisch (Ehemalige Sowjetunion)
    IRAN        = 600   # Iran
    KAZAKHSTAN  = 601   # Kasachstan
    INDONESIA   = 602   # Indonesien
    SAUDI_ARABIA= 603   # Saudi-Arabien
    VIETNAM     = 604   # Vietnam
    TURKEY      = 605   # Türkei
    # Präfix 979
    FRENCH_B    = 10    # Französisch (Belgien, Frankreich, Kanada, Luxemburg, Schweiz)
    SOUTH_KOREA = 11    # Südkorea
    ITALY       = 12    # Italien
    USA         = 8     # USA