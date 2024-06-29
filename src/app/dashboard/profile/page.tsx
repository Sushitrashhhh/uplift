'use client'

import { ProfileStats } from '@/src/app/components/ProfileStats'
import { Press_Start_2P } from 'next/font/google'
import Loader from '@/src/app/components/TextLoader'
import { Shiba } from "../../components/Shiba";
import { BottomNavigation } from '../../components/BottomNavigation'
import { useState, useEffect } from 'react';
import url from '@/config'

const pressStart2P = Press_Start_2P({
  subsets: ['latin'],
  weight: '400'
})


export default function DashboardPage() {
  const texts = ["Clash of GYMS", "Gym together", "Fitness"];
  const [username, setUsername] = useState('Faggot')

  useEffect(function () {
    fetch(url + '/user/stats', {})
      .then((resp) => resp.json())
      .then((data) => {
        console.log('bye')
        console.log(data)
        setUsername(data.username)
        console.log(username)
      })
    console.log("kms")
  }, [])
  console.log('hi')

  return (
    <div>
      <section className='flex flex-col items-center justify-center py-10'>
        <h1 className='text-center text-9xl font-extrabold leading-tight'>

          <span className={`text-center text-9xl font-extrabold leading-tight ${pressStart2P.className} bg-span-bg bg-clip-text text-transparent`}>
            uplift
          </span>
          <br />
        </h1>
        <div className='h-16'>
          <Loader texts={texts} typingSpeed={150} pauseTime={2000} />
        </div>
      </section>
      <Shiba />
      <section className='flex flex-col items-center justify-center py-10'>
        <div>
          <ProfileStats username={username} />
          <div style={{ marginBottom: '20px' }}></div>
        </div>
        <div>
          <ProfileStats username={username} />
        </div>

      </section>
      <BottomNavigation />
    </div>
  )
}