class Appointment < ApplicationRecord
  has_and_belongs_to_many :cptcodes, foreign_key: "cptcodes_id"
end
