class CreateAppointments < ActiveRecord::Migration[5.0]
  def change
    create_table :appointments do |t|
      t.string :number_of_rooms
      t.string :procedure
      t.string :cptstring
    end
  end
end
