class AppointmentsCptcodes < ActiveRecord::Migration[5.0]
  def change
    create_table :appointments_cptcodes, id: false do |t|
      t.belongs_to :appointments, index:true
      t.belongs_to :cptcodes, index:true
    end
  end
end
