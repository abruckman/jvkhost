class CreateCptcodes < ActiveRecord::Migration[5.0]
  def change
    create_table :cptcodes do |t|
      t.string "name"
    end
  end
end
