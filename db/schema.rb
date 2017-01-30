# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170129222358) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "appointments", force: :cascade do |t|
    t.string "number_of_rooms"
    t.string "procedure"
    t.string "cptstring"
  end

  create_table "appointments_cptcodes", id: false, force: :cascade do |t|
    t.integer "appointments_id"
    t.integer "cptcodes_id"
    t.index ["appointments_id"], name: "index_appointments_cptcodes_on_appointments_id", using: :btree
    t.index ["cptcodes_id"], name: "index_appointments_cptcodes_on_cptcodes_id", using: :btree
  end

  create_table "cptcodes", force: :cascade do |t|
    t.string "name"
  end

end
