import React, { Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

function Model(props) {
  // Path must be relative to the 'public' folder
  const { scene } = useGLTF('/machine.glb');
  return <primitive object={scene} {...props} />;
}

export default function Viewer3D() {
  return (
    <Canvas camera={{ position: [0, 2, 5], fov: 50 }}>
      {/* Lights */}
      <ambientLight intensity={1.5} />
      <directionalLight position={[3, 5, 2]} intensity={1} />
      <pointLight position={[-5, -5, -5]} intensity={0.5} />

      {/* Helper to visualize the scene */}
      <gridHelper />

      {/* The 3D model, with a suspense fallback */}
      <Suspense fallback={null}>
        <Model scale={1.0} />
      </Suspense>

      {/* Controls to move the camera */}
      <OrbitControls />
    </Canvas>
  );
}