import arcade

#abrir ventana
arcade.open_window(600, 600, "Drawing example")

#establecer color de fondo
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.csscolor.GREEN)

#casa
#fachada
arcade.draw_rectangle_filled(200, 300, 200, 200, arcade.csscolor.YELLOW)
#puerta
arcade.draw_rectangle_filled(200, 250, 50, 100, arcade.csscolor.BROWN)
#ventanas
arcade.draw_rectangle_filled(150, 350, 50, 50, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(250, 350, 50, 50, arcade.csscolor.BLUE)
#tejado
arcade.draw_triangle_filled(100, 400, 200, 500, 300, 400, arcade.csscolor.RED)
arcade.draw_circle_filled(200, 435, 25, arcade.csscolor.BLUE)

#arbol
arcade.draw_rectangle_filled(450, 250, 25, 100, arcade.csscolor.BROWN)
arcade.draw_triangle_filled(350, 250, 550, 250, 450, 350, arcade.csscolor.GREENYELLOW)
arcade.draw_triangle_filled(350, 300, 550, 300, 450, 400, arcade.csscolor.GREENYELLOW)
arcade.draw_triangle_filled(375, 350, 525, 350, 450, 420, arcade.csscolor.GREENYELLOW)

#rayos del sol
arcade.draw_line(75, 525, 5, 525, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 150, 525, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 75, 450, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 75, 595, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 135.5, 465.5, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 135.5, 585.75, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 25, 465.5, arcade.color.ORANGE, 3)
arcade.draw_line(75, 525, 25, 585.75, arcade.color.ORANGE, 3)

#sol
arcade.draw_circle_filled(75, 525, 50, arcade.csscolor.YELLOW)

#nube
arcade.draw_circle_filled(375, 500, 35, arcade.csscolor.WHITE)
arcade.draw_circle_filled(405, 500, 35, arcade.csscolor.WHITE)
arcade.draw_circle_filled(435, 500, 35, arcade.csscolor.WHITE)
arcade.draw_circle_filled(465, 500, 35, arcade.csscolor.WHITE)
arcade.finish_render()

#ejecutar la ventana
arcade.run()