from homeassistant.const import EntityCategory

SENSOR_DEFINITIONS = {
"ALERT_SENSORS":
    {   
        "insert tray":
        {
            "display_name": "Alarm - Insert Drip Tray",
            # "icon": "mdi:tray",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "fill water":
        {
            "display_name": "Alarm - Fill Water Tank",
            # "icon": "mdi:water",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "empty grounds":
        {
            "display_name": "Alarm - Empty Coffee Grounds",
            # "icon": "mdi:delete",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "empty tray":
        {
            "display_name": "Alarm - Empty Drip Tray",
            # "icon": "mdi:tray-alert",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "cleaning alert":
        {
            "display_name": "Alarm - Machine Cleaning Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "filter alert":
        {
            "display_name": "Alarm - Filter Change Needed",
            # "icon": "mdi:air-filter",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        }, 
        "cappu rinse alert":
        {
            "display_name": "Alarm - Milk System Rinse Needed",
            # "icon": "mdi:cup-water",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "cappu clean alert":
        {
            "display_name": "Alarm - Milk System Cleaning Needed",
            # "icon": "mdi:cup-water",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Coffee Eye (cup detected)":
        {
            "display_name": "Info - Coffee Eye (cup detected)",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Info - cappu clean alert":
        {
            "display_name": "Alarm - Info - Milk System Cleaning Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Info - coffee clean alert":
        {
            "display_name": "Alarm - Info - Machine Cleaning Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Info - decalc alert":
        {
            "display_name": "Alarm - Info - Descaling Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Info - filter used up alert":
        {
            "display_name": "Alarm - Info - Filter Change Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "LockedKeys":
        {
            "display_name": "Info - Buttons Are Locked",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "ML/OZ status":
        {
            "display_name": "Info - ML/OZ status",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "Open Tap":
        {
            "display_name": "Info - Open Tap",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "RemoteScreen":
        {
            "display_name": "Info - Remote Screen Active",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "SwitchOff Delay active":
        {
            "display_name": "Info - Machine is powering off",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "active RF filter":
        {
            "display_name": "Info - Filter Installed",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "close front cover":
        {
            "display_name": "Alarm - Close Front Flap",
            # "icon": "mdi:arrow-down-drop-circle",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "close powder cover":
        {
            "display_name": "Alarm - Close Powder Cover",
            # "icon": "mdi:cup",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "close tab":
        {
            "display_name": "Alarm - Close Tab",
            # "icon": "mdi:color-helper",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "coffee ready":
        {
            "display_name": "Info - Coffee Ready",
            # "icon": "mdi:coffee-to-go",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "coffee rinsing":
        {
            "display_name": "Info - Coffee Rinsing",
            # "icon": "mdi:cup-water",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "decalc alert":
        {
            "display_name": "Alarm - Descaling Needed",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "empty grounds RTC":
        {
            "display_name": "Alarm - Empty Grounds RTC",
            # "icon": "mdi:washing-machine",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "energy safe":
        {
            "display_name": "Info - Energy Save Mode",
            # "icon": "mdi:power-settings",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "enjoy product":
        {
            "display_name": "Info - Enjoy Product",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "error milk (milk sensor)":
        {
            "display_name": "Alarm - error milk (milk sensor)",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "error status":
        {
            "display_name": "Alarm - error status",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "fill powder":
        {
            "display_name": "Alarm - Add Grounde Coffee",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "fill system":
        {
            "display_name": "Alarm - Fill System",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "goodbye":
        {
            "display_name": "Info - Shutting Down",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "heating up":
        {
            "display_name": "Info - Heating Up",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "insert coffee bin":
        {
            "display_name": "Alarm - Insert Coffee Bin",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "left bean alert":
        {
            "display_name": "Alarm - Left Bean Empty",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "milk alert":
        {
            "display_name": "Alarm - Milk Container Empty",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "no beans":
        {
            "display_name": "Alarm - Fill Beans Container",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "no milk (milk sensor)":
        {
            "display_name": "Alarm - Milk Container Empty (milk sensor)",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "no signal (milk sensor)":
        {
            "display_name": "Alarm - Milk Cooler Connection Lost",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "not enough powder":
        {
            "display_name": "Alarm - Not Enough Ground Coffee",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "outlet missing":
        {
            "display_name": "Alarm - Outlet Missing",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "periphery alert":
        {
            "display_name": "Alarm - Accessory Alert",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "please wait":
        {
            "display_name": "Info - Machine in operation",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "powder product":
        {
            "display_name": "Info - Preparing product with ground coffee",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "press rinse":
        {
            "display_name": "Alarm - Rinse Needed",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "program-mode status":
        {
            "display_name": "Info - Machine in programming mode",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "rear cover missing":
        {
            "display_name": "Alarm - Rear Service Cover Missing",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "remove water tank":
        {
            "display_name": "Alarm - Remove Water Tank",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "right bean alert":
        {
            "display_name": "Alarm - Right Bean Container Empty",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "steam ready":
        {
            "display_name": "Info - Steam Ready",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "system emptying":
        {
            "display_name": "Info - System Emptying",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "system filling":
        {
            "display_name": "Info - System Is Filling",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "ventilation closed":
        {
            "display_name": "Alarm - Ventilation Slots Are Closed",
            # "icon": "mdi:circle-outline",
            "device_class": "problem",
            "entity_category": EntityCategory.DIAGNOSTIC,
        },
        "welcome":
        {
            "display_name": "Info - Welcome",
            # "icon": "mdi:circle-outline",
            "device_class": None,
            "entity_category": EntityCategory.DIAGNOSTIC,
        }
    },

"MAINTENANCE_COUNTERS" :
    {
    # Maintenance alerts (these are normal maintenance operations)
        "Cleaning":
        {
            "display_name": "MNT Cleanings",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "FilterChange":
        {
            "display_name": "MNT Filter Changes",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "Decalc":
        {
            "display_name": "MNT Descalings",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "CappuRinse":
        {
            "display_name": "MNT Milk Rinses",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "CoffeeRinse":
        {
            "display_name": "MNT Coffee Rinses",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "CappuClean":
        {
            "display_name": "MNT Milk Cleanings",
            "icon": "mdi:wrench",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "times",
            "state_class": "total_increasing",
        },
    },

"MAINTENANCE_PERCENTS":
    {
    # Maintenance alerts (these are normal maintenance operations)
        "Cleaning":
        {
            "display_name": "MNT % Cleaning",
            "icon": "mdi:percent",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "%",
            "state_class": "total",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "FilterChange":
        {
            "display_name": "MNT % Filter Change",
            "icon": "mdi:percent",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "%",
            "state_class": "total",
        },
        # Maintenance alerts (these are normal maintenance operations)
        "Decalc":
        {
            "display_name": "MNT % Decalc",
            "icon": "mdi:percent",
            "entity_category": EntityCategory.DIAGNOSTIC,
            "unit": "%",
            "state_class": "total",
        }
    },

"PRODUCTS":
    {
        "1 coffee special":
        {
            "display_name": "1 coffee special",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "1 Cortado":
        {
            "display_name": "1 Cortado",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "1 Cortado":
        {
            "display_name": "1 Cortado",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "1 Flat White":
        {
            "display_name": "1 Flat White",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "1 Hotwater Portion(Green tea)":
        {
            "display_name": "1 Hotwater Portion(Green tea)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "2 Americano":
        {
            "display_name": "2 Americano",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Barista Lungo":
        {
            "display_name": "2 Barista Lungo",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Cafe Barista":
        {
            "display_name": "2 Cafe Barista",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Cappuccini":
        {
            "display_name": "2 Cappuccini",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Cappuccino":
        {
            "display_name": "2 Cappuccino",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Coffee":
        {
            "display_name": "2 Coffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 coffee special":
        {
            "display_name": "2 coffee special",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Coffee Speed 1":
        {
            "display_name": "2 Coffee Speed 1",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2*Coffee Speed 1":
        {
            "display_name": "2*Coffee Speed 1",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Coffee Speed 2":
        {
            "display_name": "2 Coffee Speed 2",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2*Coffee Speed 2":
        {
            "display_name": "2*Coffee Speed 2",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Cortado":
        {
            "display_name": "2 Cortado",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Espressi":
        {
            "display_name": "2 Espressi",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Espresso Macchiati":
        {
            "display_name": "2 Espresso Macchiati",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Espresso Macchiato":
        {
            "display_name": "2 Espresso Macchiato",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Flat White":
        {
            "display_name": "2 Flat White",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Latte Macchiati":
        {
            "display_name": "2 Latte Macchiati",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Latte Macchiato":
        {
            "display_name": "2 Latte Macchiato",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Milkcoffee":
        {
            "display_name": "2 Milkcoffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2 Milk Foam":
        {
            "display_name": "2 Milk Foam",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "2 Milk":
        {
            "display_name": "2 Milk",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "2 Milk Portion":
        {
            "display_name": "2 Milk Portion",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "2 Portion Milk":
        {
            "display_name": "2 Portion Milk",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "2 Ristretti":
        {
            "display_name": "2 Ristretti",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2 Ristretti (only JOE)":
        {
            "display_name": "2 Ristretti (only JOE)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2x Americano":
        {
            "display_name": "2x Americano",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2x Cappuccino":
        {
            "display_name": "2x Cappuccino",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2x Coffee":
        {
            "display_name": "2x Coffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2x Cortado":
        {
            "display_name": "2x Cortado",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2x Espresso":
        {
            "display_name": "2x Espresso",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2x Flat White":
        {
            "display_name": "2x Flat White",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2x Latte Macchiato":
        {
            "display_name": "2x Latte Macchiato",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2x Lungo":
        {
            "display_name": "2x Lungo",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "2x Milkcoffee":
        {
            "display_name": "2x Milkcoffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "2x Milk Foam":
        {
            "display_name": "2x Milk Foam",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "2x Milk":
        {
            "display_name": "2x Milk",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "Americano":
        {
            "display_name": "Americano",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Barista Lungo":
        {
            "display_name": "Barista Lungo",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Barista Lungo (JOE ONLY)":
        {
            "display_name": "Barista Lungo (JOE ONLY)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Barista Lungo (only JOE)":
        {
            "display_name": "Barista Lungo (only JOE)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cafe Barista / Americano":
        {
            "display_name": "Cafe Barista / Americano",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cafe Barista":
        {
            "display_name": "Cafe Barista",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cafe Barista (JOE ONLY)":
        {
            "display_name": "Cafe Barista (JOE ONLY)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cafe Barista (only JOE)":
        {
            "display_name": "Cafe Barista (only JOE)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cappuccino Big":
        {
            "display_name": "Cappuccino Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Cappuccino":
        {
            "display_name": "Cappuccino",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Coffee Big":
        {
            "display_name": "Coffee Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Coffee":
        {
            "display_name": "Coffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Coffee Special":
        {
            "display_name": "Coffee Special",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Coffee Speed 1":
        {
            "display_name": "Coffee Speed 1",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Coffee Speed 2":
        {
            "display_name": "Coffee Speed 2",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Cortado":
        {
            "display_name": "Cortado",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Espresso Big":
        {
            "display_name": "Espresso Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Espresso":
        {
            "display_name": "Espresso",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Espresso Doppio":
        {
            "display_name": "Espresso Doppio",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Espresso Doppio":
        {
            "display_name": "Espresso Doppio",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Espresso Doppio (only JOE)":
        {
            "display_name": "Espresso Doppio (only JOE)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Espresso Macchiato":
        {
            "display_name": "Espresso Macchiato",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Flat White":
        {
            "display_name": "Flat White",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Hotwater Portion big":
        {
            "display_name": "Hotwater Portion big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Hotwater Portion Big":
        {
            "display_name": "Hotwater Portion Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Hotwater Portion(black tea)":
        {
            "display_name": "Hotwater Portion(black tea)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Hotwater Portion(Green tea)":
        {
            "display_name": "Hotwater Portion(Green tea)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Hotwater Portion(normal)":
        {
            "display_name": "Hotwater Portion(normal)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Hotwater Portion":
        {
            "display_name": "Hotwater Portion",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "water": True,
        },
        "Latte Macchiato Big":
        {
            "display_name": "Latte Macchiato Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Latte Macchiato":
        {
            "display_name": "Latte Macchiato",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Lungo":
        {
            "display_name": "Lungo",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Milk Big":
        {
            "display_name": "Milk Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "Milkcoffee Big":
        {
            "display_name": "Milkcoffee Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Milkcoffee":
        {
            "display_name": "Milkcoffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Milk Foam":
        {
            "display_name": "Milk Foam",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "Milk":
        {
            "display_name": "Milk",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "Milk Portion":
        {
            "display_name": "Milk Portion",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
        },
        "Pot 2 Speed":
        {
            "display_name": "Pot 2 Speed",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Pot Big":
        {
            "display_name": "Pot Big",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Pot":
        {
            "display_name": "Pot",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Powderproduct":
        {
            "display_name": "Powderproduct",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "RAF Coffee":
        {
            "display_name": "RAF Coffee",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
        "Ristretto":
        {
            "display_name": "Ristretto",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Ristretto (only JOE)":
        {
            "display_name": "Ristretto (only JOE)",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "coffee": True,
        },
        "Sweet Latte":
        {
            "display_name": "Sweet Latte",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee-outline",
            "milk": True,
            "coffee": True,
        },
},

"TOTAL_PRODUCTS":
    {
    # Maintenance alerts (these are normal maintenance operations)
        "Total Products":
        {
            "display_name": "Total Products",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee",
        },
        "Total Coffee Only":
        {
            "display_name": "Total Coffee Only",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee",
        },
        "Total Coffee With Milk":
        {
            "display_name": "Total Coffee With Milk",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee",
        },
        "Total Milk Only":
        {
            "display_name": "Total Milk Only",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee",
        },
        "Total Water Only":
        {
            "display_name": "Total Water Only",
            "unit": "products",
            "state_class": "total_increasing",
            "icon": "mdi:coffee",
        },

    }
}



