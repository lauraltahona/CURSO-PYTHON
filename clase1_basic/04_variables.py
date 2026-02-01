my_name = "Laura"
print(my_name);

age = 20
print(age);

#se puede reasignar el valor de una variable
age = 21
print(age);

#tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
# no se tiene que declarar explicitamente
name = "laura"
print(type(name));
name = 32
print(type(name));

# esto se puede hacer pero no es recomendable
name, age, is_student = "Laura", 20, True

# python no tiene constantes, pero por convención se usan mayusculas para nombrarlas
# se puede simular y se usa UPPER_SNAKE_CASE
MAX_AGE = 100
PI = 3.1416

# en la configuracion se puede poner para que no se puedan reasignar una variable de diferente tipo
is_user_logged_in: bool = False
print(is_user_logged_in);

# is_user_logged_in = "yes"  # esto SOLO avisaria si se cambia la opcion de typecheck a strict
# pero no marca error en tiempo de ejecucion, ya que python no tiene tipado estatico, sino tipado dinamico