class Cptcode < ApplicationRecord
  has_and_belongs_to_many :appointments, foreign_key: "cptcodes_id"
end
