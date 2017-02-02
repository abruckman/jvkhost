Rails.application.routes.draw do
  resources :appointments

  get '/cptcodes/make_cpts', to: 'cptcodes#make_cpts'
  root to: "appointments#new"

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
