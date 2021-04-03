"""Project
   @authors Christopher Haen cmh6674@rit.edu 
      Steven Guan sxg8944@rit.edu
"""
import os
import shutil
import math
import pandas as pd

CONTRIBUTING: {'PASSING OR LANE USAGE IMPROPER', '1', 'OTHER ELECTRONIC DEVICE', 'PAVEMENT DEFECTIVE', 'FATIGUED/DROWSY', 'TEXTING', 'CELL PHONE (HANDS-FREE)', 'TURNING IMPROPERLY', 'PHYSICAL DISABILITY', 'EATING OR DRINKING', 'OTHER LIGHTING DEFECTS', 'BACKING UNSAFELY', 'LISTENING/USING HEADPHONES', 'TINTED WINDOWS', 'WINDSHIELD INADEQUATE', 'REACTION TO OTHER UNINVOLVED VEHICLE', 'AGGRESSIVE DRIVING/ROAD RAGE', 'PEDESTRIAN/BICYCLIST/OTHER PEDESTRIAN ERROR/CONFUSION', 'OBSTRUCTION/DEBRIS', 'ILLNES', 'FOLLOWING TOO CLOSELY', 'CELL PHONE (HAND-HELD)', '80', 'OVERSIZED VEHICLE', 'DRIVERLESS/RUNAWAY VEHICLE', 'ANIMALS ACTION', 'UNSAFE SPEED', 'GLARE', 'ACCELERATOR DEFECTIVE', 'LOST CONSCIOUSNESS', 'FELL ASLEEP', 'PASSING TOO CLOSELY', 'HEADLIGHTS DEFECTIVE', 'OUTSIDE CAR DISTRACTION', 'VIEW OBSTRUCTED/LIMITED', 'TIRE FAILURE/INADEQUATE', 'DRIVER INATTENTION/DISTRACTION', 'USING ON BOARD NAVIGATION DEVICE', 'VEHICLE VANDALISM', 'LANE MARKING IMPROPER/INADEQUATE', 'UNSPECIFIED', 'REACTION TO UNINVOLVED VEHICLE', 'SHOULDERS DEFECTIVE/IMPROPER', 'PAVEMENT SLIPPERY', 'UNSAFE LANE CHANGING', 'DRUGS (ILLEGAL)', 'DRIVER INEXPERIENCE', 'PASSENGER DISTRACTION', 'ALCOHOL INVOLVEMENT', 'STEERING FAILURE', 'PRESCRIPTION MEDICATION', 'TRAFFIC CONTROL DEVICE IMPROPER/NON-WORKING', 'FAILURE TO KEEP RIGHT', 'ILLNESS', 'TRAFFIC CONTROL DISREGARDED', 'FAILURE TO YIELD RIGHT-OF-WAY', 'TOW HITCH DEFECTIVE', 'OTHER VEHICULAR', 'BRAKES DEFECTIVE'}
VEHICLE: {'ALL-TERRAIN VEHICLE', 'ATV P', 'TUGGE', 'TRASH', 'YW', 'GENE', 'SUBURBAN', 'ARIEL', 'MOVING VAN', 'FDNY ENGIN', 'INTERNATIO', 'UHAUL', 'FIRE TRUCK', 'UNNKO', 'BOX M', 'TRUC', 'FDNY AMBUL', 'ELEC', 'TR/C', 'TRACTOR TRUCK DIESEL', 'TOW TRICK', '4DR', 'ELETR', 'PIGGY BACK', 'UNATTACHED', '315 E', '72000', 'E SCO', 'MAN L', 'FUEL', 'TAXI', 'SPC', 'E COM', 'WASTE', 'BK', 'MESSAGE SI', 'ROAD', 'IP', 'RUBBE', 'TRALI', 'HUMME', 'GOVERNMENT', 'UHAUL VAN', '2 DOO', 'MAC F', 'BLACK', 'DUMPSTER', 'TANKER', 'BROWN', 'WANC', 'TRK', 'POLICE VEH', 'COMPA', 'AMBUL', 'TRUCK', 'VAN S', 'NYC FIRE T', 'MC', 'METAL', 'SEMI TRAIL', '2 HOR', 'FDNY #226', 'PICKUP TRU', 'DELIE', 'MOTOR SCOO', 'LIEBH', '4DS', 'LIGHT TOWE', 'SKIDSTEERL', 'G1', 'TANDU', 'TLC', 'P/V', 'BUS Y', 'CLUB', 'SUBN WHI', 'GAS SCOOTE', 'GLNEN', 'RAM PROMAS', 'SPORT UTILITY / STATION WAGON', 'RYDER', 'AMUBULANCE', 'ME/BE', 'YALE', 'BOBCAT', 'TOW R', 'MTA BUS  4', 'LOG', 'DEIV', 'TOYOT', 'MO-PE', '11111', 'UTILITY TR', 'FDNY TRUCK', 'SMALL', 'ACCEE', 'BED T', 'MOPED ELEC', 'TRACK', 'CONTR', 'CAMP', 'ROAD SWEEP', 'CARRI', 'WORK', 'FORK LIFT', 'ROLLE', '1', 'CHVEY', 'SCAVA', 'STAKE OR RACK', 'ENCLOSED BODY - NONREMOVABLE ENCLOSURE', 'LADDER 34', 'PICKUP TOW', 'SMALL COM VEH(4 TIRES) ', 'VMS T', 'PALLET JAC', 'LTR', 'ECOLI', 'EMS B', 'LCOMM', 'CB534', 'TOWTR', 'FIRE ENGIN', 'FD TR', 'FDNY', 'HOPPER', 'BMW MOPED', '12 FE', 'ICE C', 'E-SCOTER', 'DOT #', 'ELECT', 'WHBL', 'GARBAGE OR REFUSE', 'AP', 'ASPHA', 'CHERRY PIC', 'ULITI', 'FLED', 'NYCHA', 'PUMPER TRU', 'BOOM CRANE', 'HOTDO', 'MOTORCYCLE', 'ORION', '16M', 'F15', 'ESCAVATOR', 'SD', 'DARK COLOR', 'MTA B', 'ELEC', 'NYU S', '8X20', 'CATAPILLAR', 'BOAT', 'CONTA', 'FD LADDER', 'MOVIE', 'AMDU', '3DC-', 'AMAZON SPR', 'COMER', 'PISH', 'TOW', 'NYC', 'C2', 'CARGO TRUC', 'COM TRANS', '2DR', 'CATERPILLA', 'VEND', 'LADDE', 'VAN (', 'SHORT', 'TOKEN', 'UTILITY VE', 'E - B', 'NONE', 'SBN', 'WH FORD CO', 'TRLPM', 'REP', 'ELECTRONIC', 'DELIVERY T', 'COMM', 'POST', 'UTYLI', '18 WHEELER', 'SPEC', 'U.S.P', 'MULTI-WHEELED VEHICLE', 'AMBU', 'OLM', 'JLG M', 'RINGO', 'E TOW', 'ESCOOTER', 'DELIVERY V', 'NTTRL', 'MINI VAN', 'PUMPE', 'SPRINTER V', '2000', 'WELL DRILLER', '2 WHE', 'BLUE', 'ND', '430', 'VEH L', 'WHITE', 'UNK,', 'DEPAR', 'NYS A', 'CAT 3', 'JUNST', 'SKATEBOARD', 'REFR', 'G TOW', 'FR`', 'TTRAILER', 'ROOD', 'LIVERY VEHICLE', 'Ï¿½MBU', 'TRANSIT', 'LADDER TRU', 'COMM FOOD', 'CMS-T', '600AJ', 'VAV', 'TOWE', 'SANITATON', 'DOT V', 'BKHOE', 'TRAM', 'PUMP', 'RMB', 'JETSKI', 'BACK HOE', 'SANIT', 'FDNY EMS V', 'BEVERAGE TRUCK', 'D1', 'VAN', 'ISUZU', '4 DR SEDAN', 'UTILITY', 'INDUSTRIAL', 'CAR T', 'COACH', 'SPRINTER', 'PLOW', 'COM T', 'ARMOR', 'SURET', 'ELECR', 'C7C', 'CONCRETE M', 'VERIZ', 'MAIL TRUCK', 'POSTA', 'CMIX', 'MERCEDES', 'POWER', 'DETAC', 'E3', 'TL', 'TRIAL', 'DUMP', '3-WHE', 'SKATE', 'FLATBED TR', '00', 'REFRIGERATED VAN', 'E SKATE BO', 'FIRTRUCK', 'OIL T', '2 DR', 'E-UNICYCLE', 'WG', 'CONCR', 'BTM', 'JLG B', 'POWER LADD', 'SHORT BUS', 'DRILL RIG', 'FED EX', 'FRT', 'G COM', 'EMS TRUCK', '250-3', 'ALUMI', 'RED M', 'LIVERY BUS', 'VAM', 'APPOR', 'RD BLDNG M', 'CO', 'BLU BUS', 'SUBN TN', 'DILEVERY T', 'WORKH UTIL', 'VEHICLE 2', 'VEHIC', 'BURG', 'BIG R', 'SEAGR', 'FRIEG', 'MTA C', 'BUDGE', 'CARRY ALL', 'GLP050VXEV', 'HRSE', 'TRUCK TRAI', 'NYC TRANSI', 'USPS/GOVT', 'TR/TR', '?OMME', 'TOW TRK', 'AMBULENCE', 'UNKOW', 'FOOR', 'COM/A', 'LIMO', 'POSTO', 'DIG-I', 'LOADE', 'SUDN', 'CON ED TRU', 'SANTA', '4DSD', 'NY EMS', 'LIVERY OMN', 'PCH', 'SANITAION', 'BLOCK', 'JEEP', 'MINI', 'UTILITY WH', 'ENCLOSED BODY - REMOVABLE ENCLOSURE', 'FLAT BED', 'LIVER', 'NYC M', 'TRANSIT VA', 'OTHER', 'PAS 5', 'HARVE', 'DODGE', 'FORD', 'DEI V', 'ARMORED TR', 'DOOSK', 'SEMI-TRAIL', '7532433', 'EAMB', 'STACK', 'UKN', 'GEICO', 'PAY LOADER', 'VAN U', 'TRANSPORT', 'FLATB', 'EMT', 'EMERGANCY', 'MECHA', 'DELVIERY', 'P/SE', '26 FT', 'DUAL', 'E ONE', 'BROOM', 'FREIG', 'TOUR', 'FORK-', 'FLAT RACK', 'E-SCO', 'TOWIN', 'ATTAC', 'HOSRE', 'SCOO', 'GRAY', '4 RUN', 'CAN', 'LIGHT TRAI', 'GOVER', 'FLAT/', 'KME/F', 'POSTAL VEH', 'DEPT VAN #', 'MOTOR SKAT', 'ELECTRIC S', 'HOUSE', 'AMBULANCE', 'FLATBED', 'CONVE', 'CATE', 'USPS VAN', '0', 'LADD', 'TRACTOR', 'USPS #7530', 'JOHN DEERE', 'YY', 'FIRET TRUC', 'UHAUL TRAI', 'STAKE', 'VESPA', 'LEFT', 'FD NY', 'SANTI', 'TOYOTA', 'GREEB', 'NYC A', 'VAB', 'G PAS', 'HI TA', 'SS', 'MAXIM', 'TRUCK CRAN', '3DOOR', '985', 'SEGWA', 'WESCO', 'FEIG', 'PALFINGER', 'POSTAL CAR', 'STAK', 'SPRIN', 'AXO', 'U HAUL TRU', 'OFFIC', 'GE/SC', 'VAN H', 'PAVIN', 'SNOW', 'VANETTE', 'FDNY LADDE', 'UNKNW', 'TREE CUTTE', 'SCOOTER', 'VAN CAMPER', 'CRWZK', 'CONTI', 'MTA BUS', 'ABULA', 'PC', 'TRAI', 'UPS TRUCK', 'NYC BUS', 'SMART', 'PALLE', 'USPS POSTA', 'LIGHT', 'USPS TRUC,', 'GOLF KART', 'UHAUL TRUC', 'BOXTR', 'TR-TRAILER', 'WHEEL BARR', 'SW', 'NYC D', 'AMB', 'GOV V', '1C', 'SWEPE', '11-VA', 'FRIEGHTLIN', 'UK', 'PICK TRUCK', 'CAB', 'UTLL', 'SKID LOADE', 'G SCL', 'OMNIB', 'G  CO', 'EXCAV', 'ULILI', 'FIRER', 'FD LA', 'NYNJ RAIL', 'VAN C', 'QMZ', 'EAST', '1S', 'ESU RESCUE', 'FLAT BED T', '2003', 'BIKE', 'B5-44', 'USPS SELF', 'WHITE AMBU', 'BOB C', 'SAFET', 'SWEEPER', 'E- BI', 'MARKE', 'NYPD', 'NAT GRID T', '4 AXE', 'RENTA', 'TRACTOR TRUCK GASOLINE', 'TRAIN', 'LAWNMOWER', 'UKNOWN', 'REFRG', 'CABIN', 'MACK TRUCK', 'MCY', 'NYC AMBULA', 'PASS', 'E/BIK', 'FEDER', 'SUB', 'PICKU', 'PLATF', 'NYC-S', '00000', 'QUALITY TR', 'PASSENGER', 'VANT', 'MOTORSCOOT', 'UTV', 'TL TR', 'D/V WB', 'USPS MAIL', 'SE', 'ASTRO', 'USPCS TRUC', 'VAN F', 'VOL', 'STATION WAGON/SPORT UTILITY VEHICLE', 'EPO', 'SPECIAL PU', 'TOW TRUCK / WRECKER', 'TRUCK VAN', 'DELVI', 'WORK VAN', 'ARMY', 'TOW T', 'NT TR', 'FIRE', 'FED', 'TCN', 'SYBN', 'IMPAL', 'REFQ', 'BACKHOE', 'TOWER', 'GMC', 'PAYLO', 'LSA', 'DRONE', 'NV150', 'POWER SHOV', 'GLASS RACK', 'SPECI', 'FLAT', 'UHUAL', 'CAR C', 'D', 'PSH', 'OMT', 'DSNY', 'DUMPT', 'QUAD', 'BOBCAT 216', 'CAT32', 'BUCKE', 'RGS', 'DIRT', 'E AMB', 'GO KART', 'I1', 'SNOW PLOW', 'G AMB', 'US POSTAL', 'MOTORSCOOTER', 'MOTOR', 'AERIA', 'MOPED SCOO', 'USPS#', 'CHEVROLET', 'POSTAL TRU', 'SUBN/', 'FEDX', 'WINEB', 'COMB', 'E BIK', 'UTIL', '11 PA', '000', 'GRAIN', 'FREIH', 'ESCOVATOR', 'UNK T', 'M/A', 'AMABU', 'GATOR', 'STREET SWE', 'LUNCH WAGON', 'TANK', 'FEDERAL EX', 'T650', 'PARKE', 'DEPT', 'POST OFFIC', 'PICKUP WITH MOUNTED CAMPER', 'LIMOU', 'E250', 'GOLF CART', '9999', 'COMMERCIAL', 'GR HS', 'SANAT', 'LMA', 'VANET', 'FORD ECONO', 'AMBULANCE`', 'TRLR', 'TAN P', 'LUMBE', 'VAN TRUCK', 'CHASSIS CAB', 'MVP', 'YLL P', 'BACK', 'CATER', 'COM', 'FORLIFT', 'GOVT.', 'WAGON', 'CONCRETE MIXER', 'MOPEN', 'CUSHM', 'PLOW  TRUC', 'TLC P', 'ECOM', 'SPEC-', 'ARMORED TRUCK', 'TRUCK FLAT', 'DOT EQUIPM', '2015', 'C3', 'PEDI CAB', 'ABULANCE', 'POIS', 'VAN T', 'HWY C', 'DUMPS', 'U-HAUL', 'HORSE TRAI', 'U.S P', 'PZ', 'POLIC', 'HI-LO', 'PASSA', 'CLEAN', 'E-MOT', 'NAVIG', 'NYC B', 'UNK.', 'I-HAUL', 'FDNY FIRE', 'GARBA', 'MOBILE FOO', 'MP', 'DLVR', 'DIRTBIKE', 'E SCOOTER', 'TCR', 'TRANS', 'PICK', 'USPST', 'YELLO', '3-DOOR', 'TKTR', 'FORKLIFT', 'NEW Y', 'SHOVE', 'MOPED/SCOO', 'AMULA', 'INTE TRUCK', 'BED', 'RV/TR', 'JLG L', 'HINO TANK', 'SCHO', 'EMS/VAN', 'US MA', 'TILT TANDE', 'LIFT', 'UTIL.', 'ACCESS A R', 'JOHND', 'FRE T', 'MOTORIZEDS', 'SUBN', 'AM/TR', '4SEDN', 'FORD SPRIN', 'SEMITRAILE', 'TRACTOR TR', 'CAMPE', 'MOPD', 'TRAC', 'MACK', 'R/V', 'U-HAU', 'SKID', 'FLATBED FR', 'G1', 'NYC EMS', 'NO/BU', 'RENTAL TRU', 'TRACT', 'UNLNO', 'OTH', 'REFG/', 'TRC M', 'HAUL FOR H', 'GRAIL', 'HAND', 'TRC', 'REF G', 'DIESE', 'PICK UP', 'TOWE TRUCK', 'C1', 'DELV.', 'SHCOO', 'MOPET', 'USPS', 'MOTOR HOME', 'BULLDOZER', 'GAS T', 'UTILITY.', 'SEM', 'TK', 'ENGIN', 'ESCOO', 'SMART CAR', 'SNOWMOBILE', 'PEDICAB', 'DB', 'G PSD', '99999', 'U-TRU', 'CAR', 'UNKN', 'LIVESTOCK RACK', 'FLAT  BED', 'CONST EQUI', 'LIBER', 'A-ONE', 'CITY OF NE', 'CAMPER TRA', 'SUV /', 'ROADS', 'PALLET', 'PAS', 'YELLOW CAB', 'SEN', '2 DR SEDAN', 'L1', 'TKP', 'DELIVERY', 'EXPRE', '3 DOO', 'H3', 'UNKNOWN VE', 'ICECR', 'PASSE', 'GMC V', '.', 'STREET CLE', 'DELIV', 'BOX P', 'E-SCOOTER', 'NISSA', 'COMMU', 'VAN FORD', 'SPINTER VA', 'ECONO', 'PSP', '2- TO', '4DOOR', 'LUV', '4D', 'PK', 'GMC T', 'SKYWATCH', '197209', 'FORKL', 'JCB40', 'COMIX', 'CEMEN', 'AMULANCE', 'BOBCA', 'BOOM LIFT', 'ANBUL', 'UTILITY VA', 'RANGE', 'FD TRUCK', 'TT', 'SRF', 'GRUMM', 'FOLK LIFT', 'BOX H', 'HOE-L', 'LAWN', 'G SEM', 'E-SKA', 'GENIE', 'EMRGN', 'BUS', 'N?A', 'RDS', 'T630 FORKL', 'BOX TRUCK', 'VAN W', '(CEME', 'E-SOOTER', 'PASSENGER VEHICLE', 'GARBAGE TR', 'AMAZON TRU', 'SCHOOL VAN', 'U HAU', 'ECONOLINE', 'MOT S', 'PUSH', 'TC', 'TRLR PLT,', 'GREEN', 'ST', '38AB-', 'MTA', 'EXCAVATOR', 'DIRTB', 'DEL', 'E REVEL SC', 'RORO', 'SPECIAL CO', 'REFUSE TRU', 'VENDOR CHA', 'UNKNOW', 'HD TO', 'MTA V', 'TCM', 'N/A', 'TR', 'PICK UP TR', 'TRAIL', 'C-1', 'CART', 'LEFT THE S', 'BOOM', 'UNKOWN', '5X8 T', 'AMBULETTE', 'RAZOR', 'PRIVA', 'NYC F', 'DOT T', '2 TON', 'MAC T', 'FRONT-LOAD', 'REFG', 'CHEVY', 'C 1', 'ELECTRIC M', 'RED,', 'RAZOR SCOO', 'D3', 'UBER', 'SCHOOLBUS', 'RAM', 'RD/S', 'OML', 'FDNY FIRET', 'P/SH', 'CAT.', 'SLINGSHOT', '12 PA', 'CT', 'MINIV', 'CONV', 'DUMP TRUCK', 'USPS2', 'FIRETRUCK', 'BACKHOE LO', 'VAN/B', 'CHART', 'UTIL WH', 'FREIGHTLIN', 'MOBILE', 'EC2', 'NOT I', 'TF', 'SANITATION', 'NYC ACS VA', 'HEIL', 'UT', 'MINIBIKE', 'J1', 'FUSION', 'EMS AMBULA', 'CROSS', 'GOKAR', 'FARM', 'WHIT', 'RESCU', 'HEAVY', 'FOOD', 'PICK-', 'R/V C', 'FLEET', 'MCY B', 'C0MME', 'RV/VAN', 'MTRIZ', 'KME', 'HINO', 'ITAS', 'GARAB', 'FIRET', 'FREIG DELV', 'TR/KI', 'T/ CR', 'HD', '994', 'DOLLY', 'GOLF', 'U-HAL', 'VAN A', 'BOBCAT FOR', 'CONT-', 'WORKM', 'VAN/R', 'RMP V', 'SCOTTER', 'UTILT', 'E350', 'OMT/T', 'LCOM', 'FREE', 'VMS', 'ST150', 'OZ MO', 'CM', 'CEMENT TRU', 'CITY MTA B', 'APURP', 'SCOOC', 'PASS-', 'KEN', 'TLR', 'PICK-UP TR', 'FLTRL', 'SGWS', 'CHURC', 'OMR', 'F-250', 'PLOW TRUCK', 'GLBEN', 'PARCE', 'TILLA', 'DEMA-', 'LMB', 'MO PE', 'KUBOT', 'HIGHL', 'VANG', 'UNKNOWN', 'MAC 1', 'DLEV', 'WINNE', 'MTA TRUCK', '18 WH', 'MINICYCLE', 'LMTV', 'APP C', 'HDC', 'FRH', 'BUCKET TRU', 'PRKS', 'UTLIT', 'MO PA', 'PETER', 'DIRT-', 'COURI', 'MOTORBIKE', 'F350', 'E-BIKE', 'CAT P', 'MTA U', 'OMNIBUS', 'CAT', 'TUCK', 'EMS H', 'KP160', 'LIFT BOOM', 'ROLLI', 'UNKL', 'HOUSE ON W', 'BOX T', 'MOTER', 'GEN  AMBUL', 'EMERGENCY', 'OLC', 'BUSS', 'GOVT', 'SEMI', 'TRIM', 'ESU T', 'CITY OWNED', 'TOWMA', 'TANK WH', 'SELF-', 'FORTL', 'AMBULACE', 'SILVE', 'INTER', 'CITY', 'VS2', 'UHAL', 'SIERRA', 'E- MOTOR B', 'YW PO', 'CHEV', 'US GO', 'TRAC.', 'LLV MAIL T', 'BACKH', 'REVEL', 'FREIGHT', 'BOB CAT', 'MTA T', 'YPS', 'LIT DIRECT', 'SUV', 'REFRI', 'TTAILER', 'S/SP', 'TRAILER', 'NYC SANITA', 'CONST', 'PUSH SCOOT', 'SEMI-', 'CAT 4', 'REVEL SCOO', 'MARK', 'HISTORICAL', 'PROGR', 'E-BIK', 'DHL T', 'FORK', 'ES', 'USPS # 487', 'DEL T', 'MARKED VAN', 'LULL', 'SCAFF', 'SUBR', 'OPEN BODY', 'U.S. POSTA', 'E', 'SEA', 'FDNY EMT', 'BULLD', 'FLAT-', 'PAS V', 'NYC G', 'NIU', 'FDNY EMS', 'FRONT', 'BULK AGRICULTURE', 'POSTAL VAN', 'TRL', 'SCHOO', 'COM V', 'COM.', 'TRA/R', 'WHEEL', 'ACCES', 'ENCLO', 'PSR', 'TOW TRUCK', 'US GOVT VE', 'YELLOWPOWE', 'CASE', 'BOOML', 'TRT', 'USPOS', 'APORT', 'VAN`', 'VAN/', 'BARRI', 'YAMAH', 'POSTAL BUS', '52? T', 'MILLI', 'MAIL', 'LLV', 'ART M', 'STATE', 'SFI', 'CONT', 'MOBIL', 'DEAGR', 'LTRL', 'E PAS', 'PKUP', 'STERL', 'TRAILOR', 'OFF R', 'CON E', 'MOVIN', 'MAN B', 'POSTAL SER', 'FOOD CART', 'PICK RD', 'VAS', 'GENUI', 'G SPC', 'SUDAN', 'UNKNO', 'TRIALER', 'FED E', 'SCISS', 'E-350', 'DEP V', 'FRHT TRAIL', 'MI/FU', 'TIR', 'MOPED', 'UPS M', 'FLLET', '3 WHE', 'BICYCLE', 'RED T', 'BOX', 'COMM.', 'OMC', 'FORKLIFT T', 'SUBN-', 'BSD', 'VAN/TRUCK', 'CMIXER', 'DUMPE', 'FOOT', 'NYPD SIGNA', 'US', 'NYC FIRETR', 'NYC S', 'DELV', 'F650', 'LAWN MOWER', 'DOT R', 'PET', 'COLL', 'MTR S', 'H1', 'SC', 'CONSTRUCTI', 'PUMPER', 'GOV', 'KW TR', 'A', 'CHEVR', 'SCOM', 'LD', 'PORTA', 'SMALL TRAC', 'UNK', 'UHAUL BOX', 'RMP', 'ICE CREAM', 'ESU REP', 'NYFD', 'BUMP', 'TAILG', 'SUBN - AMB', '15 PA', 'LEASED AMB', 'NYS AMBULA', 'NS AM', 'FORD VAN', 'EMS A', 'HORSE', 'USP M', 'TLC V', 'CHERR', 'NAA', 'SPEAC', 'BUS M', 'SELF', 'DOT TRUCK', 'QBE I', 'COMMERICAL', 'E BIKE', 'HIGH', 'OML/', 'SALT', 'E-SKATEBOA', 'TANKE', 'SCOMM', 'E450', 'LAUND', 'VAN E', 'PSD', 'SCHOOL BUS', 'TRACK EXCA', 'INTL', 'CARGO VAN', 'CAR TRAILE', 'HI LO', 'SWT', 'UD', 'BULDOZER', 'VAN/TRANSI', 'SKID-', 'SCOOT', 'HILOW', 'HOOK', 'TOW-T', 'WC', 'F550', 'TRCIC', 'USPS 88716', '999', 'MOTORIZED HOME', 'MECHANICAL', 'SNOW PLOWE', 'TE', 'UTILI', 'UPS T', 'UNI', 'NYC FD', 'PEDIC', 'APP', 'CONVERTIBLE', 'ENGI', 'CRANE', 'LARGE COM VEH(6 OR MORE TIRES)', 'SEDAN', 'COURIER', 'CARGO', 'VN', '5', 'PICKUP', 'BOBCT', '2TON', 'CADET', 'P/U', 'T880', 'JOHN', 'SPC P', 'DUNBA', '4WHEE', 'E1', 'FDNY CHIEF', 'COMME', 'ELECTRIC B', 'COMMM', "GOV'T", 'EMS', "12' O", 'DP', 'NA', 'VPG', 'SELF INSUR', '18 WEELER', 'FRHT', 'FREIGHT FL', '013', 'BUCKETLOAD', 'POTAL', 'BS', 'E.M.S', 'MAILTRUCK', 'ALMBULANCE', 'SWEEP', 'PICK-UP TRUCK', 'USPS TRUCK', 'FEDEX', 'FRE', 'FD FI', 'US PO', 'COUPE', 'MOPAD', 'SUBUR', 'CATIP', 'PERM', 'LIMO/', 'YNK', 'CAT 9', 'FOOD TRUCK', 'VAN/T', 'G OMR', 'AMUBL', 'OMS', 'RENTED BOO', 'RV', 'HORSE CARR', 'WORKH', 'SCL', 'MINIVAN', 'PS', 'ELEC. UNIC', 'LP', 'COMM TRK', 'KENWO', '35 FT', 'DELVR', 'F150XL PIC', '\x7fOMM', 'BICYC', 'STREE', 'UNK L', 'EBIKE', 'VMS SIGN', 'REPAI', 'SM YW', 'UNK/L', 'FREIGHT TR', 'SERVI', 'TOUR BUS', 'BOBBY', 'NYC DOT', 'DLR', 'NYCTA', 'GAS S', 'UNKWN', 'DIRT BIKE', 'NV CA', 'OBJEC', 'HEARSE', 'EMS T', 'OMNI', 'PU', 'COMMAND PO', 'FARM VEHICLE', 'CHEVY EXPR'}



clean_data = True       #True to do cleaning, False to skip cleaning

file_name = "Motor_Vehicle_Collisions_-_Crashes"
file_path = "Motor_Vehicle_Collisions_-_Crashes.csv"
max_year = 2020


useful_cols = ['CRASH DATE', 'CRASH TIME', 'BOROUGH', 'LATITUDE', 'LONGITUDE',
               'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
               'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED',
               'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1',
               'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4',
               'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3',
               'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']

boroughs = ["BRONX", "BROOKLYN", "MANHATTAN", "QUEENS", "STATEN ISLAND"]
vehicles = ["SEDAN", "STATION WAGON/SPORT UTILITY VEHICLE", "TAXI", "TRAILER",
            "TRACKER TRUCK DIESEL", "BIKE"]


# vehicle
#
valid_col_vals = {
  "BOROUGH":boroughs,
  "VEHICLE":['ALL-TERRAIN VEHICLE', 'ATV P', 'YW', 'GENE', 'SUBURBAN', 'MOVING VAN', 'FDNY ENGIN', 'TRACTOR TRUCK DIESEL',
             'TOW TRICK', '4DR', 'UHAUL VAN', 'TANKER', 'NYC FIRE T', 'SPORT UTILITY / STATION WAGON', '1',
             'STAKE OR RACK', 'ENCLOSED BODY - NONREMOVABLE ENCLOSURE', 'SMALL COM VEH(4 TIRES) ', 'FD TR',
             'GARBAGE OR REFUSE', 'WH FORD CO', 'MULTI-WHEELED VEHICLE', 'WELL DRILLER', 'LIVERY VEHICLE',
             'TRANSIT', 'REFRIGERATED VAN', 'ENCLOSED BODY - REMOVABLE ENCLOSURE',
             'TRACTOR TRUCK GASOLINE', 'STATION WAGON/SPORT UTILITY VEHICLE', 'LUNCH WAGON', 'PICKUP WITH MOUNTED CAMPER',
             'ARMORED TRUCK', 'PASSENGER VEHICLE', 'TRLR PLT,', 'BULK AGRICULTURE', 'LARGE COM VEH(6 OR MORE TIRES)'],
  "CONTRIBUTING":['PASSING OR LANE USAGE IMPROPER', '1', 'OTHER ELECTRONIC DEVICE', 'PAVEMENT DEFECTIVE', 'FATIGUED/DROWSY', 'TEXTING', 'CELL PHONE (HANDS-FREE)', 'TURNING IMPROPERLY',
                  'PHYSICAL DISABILITY', 'EATING OR DRINKING', 'OTHER LIGHTING DEFECTS', 'BACKING UNSAFELY', 'LISTENING/USING HEADPHONES', 'TINTED WINDOWS', 'WINDSHIELD INADEQUATE',
                  'REACTION TO OTHER UNINVOLVED VEHICLE', 'AGGRESSIVE DRIVING/ROAD RAGE', 'PEDESTRIAN/BICYCLIST/OTHER PEDESTRIAN ERROR/CONFUSION', 'OBSTRUCTION/DEBRIS', 'FOLLOWING TOO CLOSELY',
                  'CELL PHONE (HAND-HELD)', '80', 'OVERSIZED VEHICLE', 'DRIVERLESS/RUNAWAY VEHICLE', 'ANIMALS ACTION', 'UNSAFE SPEED', 'GLARE', 'ACCELERATOR DEFECTIVE', 'LOST CONSCIOUSNESS', 'FELL ASLEEP',
                  'PASSING TOO CLOSELY', 'HEADLIGHTS DEFECTIVE', 'OUTSIDE CAR DISTRACTION', 'VIEW OBSTRUCTED/LIMITED', 'TIRE FAILURE/INADEQUATE', 'DRIVER INATTENTION/DISTRACTION', 'USING ON BOARD NAVIGATION DEVICE',
                  'VEHICLE VANDALISM', 'LANE MARKING IMPROPER/INADEQUATE', 'UNSPECIFIED', 'REACTION TO UNINVOLVED VEHICLE', 'SHOULDERS DEFECTIVE/IMPROPER',
                  'PAVEMENT SLIPPERY', 'UNSAFE LANE CHANGING', 'DRUGS (ILLEGAL)', 'DRIVER INEXPERIENCE', 'PASSENGER DISTRACTION', 'ALCOHOL INVOLVEMENT',
                  'STEERING FAILURE', 'PRESCRIPTION MEDICATION', 'TRAFFIC CONTROL DEVICE IMPROPER/NON-WORKING', 'FAILURE TO KEEP RIGHT', 'ILLNESS',
                  'TRAFFIC CONTROL DISREGARDED', 'FAILURE TO YIELD RIGHT-OF-WAY', 'TOW HITCH DEFECTIVE', 'OTHER VEHICULAR', 'BRAKES DEFECTIVE'],

}


borough_long_lat_map = {}     # average latitude and longitude for each borough

year_dict = {}                # contains <year, [(start_index, end_index)...]>



def compute_euclid_dist(valid_str:str, invalid_str:str)->int:
  valid_str_len = len(valid_str)
  invalid_str_len = len(invalid_str)

  max_len = max(valid_str_len, invalid_str_len)
  min_len = min(valid_str_len, invalid_str_len)

  sum_of_squared = 0

  for i in range(min_len):
    diff = ord(valid_str[i]) - ord(invalid_str[i])
    squared_diff = math.pow(diff,2)
    # print(valid_str[i] + " - " + invalid_str[i] + " = " + str(squared_diff))
    sum_of_squared += squared_diff

  if min_len == max_len:
    return math.sqrt(sum_of_squared)

  if invalid_str_len == min_len:
    for i in range(min_len, max_len):
      diff = ord(valid_str[i])
      squared_diff = math.pow(diff, 2)
      sum_of_squared += squared_diff
      # print(valid_str[i] + " - 0 = " + str(squared_diff))
  else:
    for i in range(min_len, max_len):
      diff = ord(invalid_str[i])
      squared_diff = math.pow(diff, 2)
      sum_of_squared += squared_diff
      # print("0 - " + invalid_str[i] + " = " + str(squared_diff))

  return math.sqrt(sum_of_squared)





def load_data():

  empty_data_frame = pd.read_csv(file_path, nrows=0)
  col_names = list(empty_data_frame.columns)

  df = pd.read_csv(file_path, names=col_names, usecols=useful_cols, skiprows=1, low_memory=False)

  print(df)

  list_of_factors_col = ['CONTRIBUTING FACTOR VEHICLE 1',
                         'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3',
                         'CONTRIBUTING FACTOR VEHICLE 4',
                         'CONTRIBUTING FACTOR VEHICLE 5']

  list_of_vehicle_col = ['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3',
                         'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']


  for col_name in list_of_vehicle_col:
    valid_vals = valid_col_vals['VEHICLE']
    val_list = df[col_name]
    len_of_list = len(val_list)

    for i in range(len_of_list):
      if pd.notna(df[col_name][i]):
        min_dist = math.inf
        min_val = ""
        for valid_val in valid_vals:
          dist = compute_euclid_dist(valid_val, df[col_name][i])

          if dist < min_dist:
            min_dist = dist
            min_val = valid_val

        df.at[i, col_name] = min_val
  for col_name in list_of_factors_col:
    valid_vals = valid_col_vals['CONTRIBUTING']
    val_list = df[col_name]
    len_of_list = len(val_list)
    # print(len_of_list)
    for i in range(len_of_list):
      if pd.notna(df[col_name][i]):
        min_dist = math.inf
        min_val = ""
        for valid_val in valid_vals:
          dist = compute_euclid_dist(valid_val, df[col_name][i])

          if dist < min_dist:
            min_dist = dist
            min_val = valid_val

        df.at[i, col_name] = min_val


  new_file_path= file_name+"_cleaned.csv"
  df.to_csv(path_or_buf=new_file_path)




def pre_clean():

  before = valid_col_vals['VEHICLE']
  new_list = []
  new_list.append(before[0])

  for x in before:

    list_len = len(new_list)
    if list_len > 0:
      min_dist = math.inf

      for i in range(list_len):
        dist = compute_euclid_dist(new_list[i], x)
        print(dist)

        if dist < min_dist:
          min_dist = dist

      if min_dist > 70:
        new_list.append(x)

  print(new_list)


def main():
  load_data()






if __name__ == "__main__":
  main()