<script setup>
import {useRoute} from 'vue-router'

const route = useRoute()
const slug = route.params.slug

import {ref, onMounted} from 'vue'
import axios from 'axios'

const apartment = ref(null)
const fetchApartment = async () => {
  const response = await axios.get(`${import.meta.env.VITE_API_URL}/apartments/apartments/${slug}/`)
  apartment.value = response.data
}
onMounted(fetchApartment)
</script>

<template>
  <div v-if="apartment" class="apartment-detail flex flex-col gap-4">
    <div class="apartment-header flex flex-col gap-1">
      <span class="apartment-name">{{ apartment.name }}</span>
      <span class="apartment-slug">{{ apartment.slug }}</span>
      <div v-if="apartment.availability">
        <span class="availability text-green-500">Available</span>
      </div>
      <div v-else>
        <span class="availability text-red-500">Not available</span>
      </div>
    </div>
    <hr>
    <div class="apartment-body flex flex-col gap-2">
      <div class="apartment-description flex flex-col gap-2">
        <span>Apartment description:</span>
        <span>{{ apartment.description }}</span>
      </div>
      <span>Owner: {{apartment.owner}}</span>
      <span>Rooms: {{ apartment.number_of_rooms }}</span>
      <span>Size: {{ apartment.square }} m²</span>
      <span>Price: ${{ apartment.price }}</span>
    </div>
  </div>
  <div v-else>
    <p>Loading details...</p>
  </div>
</template>