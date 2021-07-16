try:
    x = int( input( 'entre com um numero: ' ) )
    y = int( input( "entre com outro numero: " ) )
    print( x, '/', y, '=', x/y )
except ValueError:
    print('Não é possivel dividir números decimais! ')
except ZeroDivisionError:
    print('Não é possivel dividir números por zero! ' )
finally:
     print('Por favor continue a operação! ')