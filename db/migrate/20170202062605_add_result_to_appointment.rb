class AddResultToAppointment < ActiveRecord::Migration[5.0]
  def change
    add_column :appointments, :result, :string
  end
end
