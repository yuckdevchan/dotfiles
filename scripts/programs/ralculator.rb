require "gtk3"

window = Gtk::Window.new("First example")
window.set_size_request(400, 400)
window.set_border_width(10)

button = Gtk::Button.new(:label => "Say hello")
button.signal_connect "clicked" do |_widget|
  puts "Hello World!!"
end

class ralc(Gtk.Window)
    def __init__(self)

        self.grid = Gtk::Grid.new
        window.add(grid)

        self.seven = Gtk::Button.new(:label => "7")
        self.button.signal_connect "on_button_clicked"

        self.eight = Gtk::Button.new(:label => "8")
        self.button.signal_connect "on_button_clicked"

        self.nine = Gtk::Button.new(:label => "9")
        self.button.signal_connect "on_button_clicked"

        self.grid.attach(seven 0, 4, 1, 1)
        self.grid.attach(eight 1, 4, 1, 1)
        self.grid.attach(nine 2, 4, 1, 1)

        def on_button_clicked(self, widget)
            if widget.get_label == "C"
                self.display.set_markup("")
                self.full_query = ""
            new_entry = String::(widget.get_label)

def main
    window.add(button)
    window.signal_connect("delete-event") { |_widget| Gtk.main_quit }
    window.show_all
    Gtk.main
end

main
